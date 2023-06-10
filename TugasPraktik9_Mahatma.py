# Blok try-except-else-finally ini digunakan untuk menangkap pesan error (error message) yang muncul karena program crashed
try:
    bil1 = int(input('masukkan bilangan pertama:'))
    bil2 = int(input('masukkan bilangan kedua:'))
    hasil = bil1 + bil2
    print(hasil) 
except ValueError:
    print('Input data tidak valid')
# Bagian else akan dijalankan apabila tidak terjadi exception pada bagain try
else:
    print(hasil)
# Code Syntax ini akan tetap dijalankan, baik terjadi exception maupun tidak   
finally:
    print('Program Penjumlahan Selesai')