from yowsup.layers import YowLayerEvent, YowParallelLayer
from yowsup.layers.auth import YowAuthenticationProtocolLayer
from yowsup.layers.network import YowNetworkLayer
from yowsup.layers.protocol_messages import YowMessagesProtocolLayer
from yowsup.layers.protocol_receipts import YowReceiptProtocolLayer
from yowsup.layers.protocol_acks import YowAckProtocolLayer
from yowsup.layers.stanzaregulator import YowStanzaRegulator
from yowsup.layers.axolotl import YowAxolotlLayer
from yowsup.layers.logger import YowLoggerLayer
from yowsup.common import YowConstants

class EchoLayer(YowParallelLayer):
    def __init__(self):
        super().__init__()
        self.ackQueue = []

    def receive(self, event: YowLayerEvent):
        if event.get_event_name() == YowNetworkLayer.EVENT_STATE_CONNECT:
            layer = YowAuthenticationProtocolLayer(self.params["phone"], self.params["auth"])
            self.ackQueue.append(layer)
            self.ackQueue.insert(0, YowLoggerLayer())
            self.ackQueue.append(YowReceiptProtocolLayer())
            self.ackQueue.append(YowMessagesProtocolLayer())
            self.ackQueue.append(YowAckProtocolLayer())

            self.set_acks(self.ackQueue)

            self.broadcast(YowLayerEvent(YowNetworkLayer.EVENT_STATE_CONNECT))

        elif event.get_event_name() == YowMessagesProtocolLayer.EVENT_RECEIVE_MESSAGE:
            message = event.get_arg("message")
            message_out = "{}: {}".format(message.getFrom(False), message.getBody())
            self.toLower(YowLayerEvent(YowMessagesProtocolLayer.EVENT_SEND_MESSAGE, message_out, message.getFrom()))

if __name__ == '__main__':
    CREDENTIALS = ("YOUR_PHONE_NUMBER", "YOUR_PASSWORD") # Isi nomor WA dan password di sini

    layers = (
        EchoLayer(),
        YowAxolotlLayer,
        YowStanzaRegulator,
    )

    stack = YowParallelLayer.build(layers)

    stack.setProp(YowAuthenticationProtocolLayer.PROP_PASSIVE, True)
    stack.setProp(YowNetworkLayer.PROP_ENDPOINT, YowConstants.ENDPOINTS[0])
    stack.setProp(YowAxolotlLayer.PROP_IDENTITY_AUTOTRUST, True)

    stack.setProps(CREDENTIALS)
    stack.broadcastEvent(YowLayerEvent(YowNetworkLayer.EVENT_STATE_CONNECT))
    stack.loop()
