hitung = 0
sum = 0
print(60*"=")
print("    Program Hitung Bilangan habis dibagi 3 dan 5 [1-100]")
print(60*"=")
for i in range(100):
    bil = i + 1
    if bil % 3 == 0 and bil % 5 == 0:
        hitung = hitung + 1
        sum = sum + bil
        print("Bilangan pada index ke-",i,"Habis dibagi 3 dan 5 adalah ",bil)
print(60*"=")        
print("Banyak bilangan yang habis di bagi 3 dan 5 adalah",hitung)
print("Jumlah dari semua bilangan habis di bagi 3 dan 5 adalah",sum)