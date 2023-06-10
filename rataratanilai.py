# ini komentar
# kondisi y = true kondisi n = false
y = True
n = False
# kondisi true
while y:
    opsi = int(input(  '''
==========================================
Selamat Datang di Program Sederhana Python
==========================================
1. Persegi Panjang
2. Rata-rata Nilai
3. Cek Bilangan Ganjil Atau Genap
4. Jumlah Huruf Vokal
5. Lingkaran
6. Keluar
==========================================
Masukkan Pilihan kamu: '''))
    # Rumus Persegi Panjang
    if opsi == 1:
        print('\n')
        print(31*'=')
        print('\tPilih Rumus')
        print(31*'=')
        print('''
        1. luas
        2. keliling
        ''')
        rumus = int(input('Nama Rumus: '))
        if rumus == 1:
            panjang = int(input('Masukkan Panjang: ' ))
            lebar = int(input('Masukkan Lebar: '))
            hasil = panjang * lebar
            print('luas persegi panjang: ',hasil)
        elif rumus == 2:
            panjang = int(input('Masukkan Panjang: ' ))
            lebar = int(input('Masukkan Lebar: '))
            hasil = 2 * (panjang + lebar)
            print('keliling persegi panjang: ',hasil)
        print(31*'=')
        pilihan = input('''Coba lagi [y/n]?
        ''')
        if pilihan == 'y':
            y = True
        elif pilihan == 'n':
            n = y = n

    # Menghitung Nilai Rata rata
    elif opsi == 2:
        print('\n')
        print(41*'=')
        print("PROGRAM PYTHON MENGHITUNG NILAI RATA-RATA")
        print(41*'=')
        ni = int(input("\nBanyaknya Data Nilai: "))
        print() #Membuat baris baru
        data = []
        jum = 0
        for i in range(0, ni):
            temp = int(input("Masukkan Nilai ke-%d: " % (i+1)))
            data.append(temp)
            jum += data[i]
            rata2 = jum / ni
        print("\nNilai Rata-rata  = %0.2f" % rata2)
        print(41*'=')
        pilihan = input('''Coba lagi [y/n]?
        ''')
        if pilihan == 'y':
            y = True
        elif pilihan == 'n':
            n = y = n
    # cek bilangan ganjil/genap        
    elif opsi == 3:
        print('\n')
        print(40*'=')
        print('Program Cek Bilangan Ganjil/Genap')
        print(40*'=')
        bilangan = int(input('Masukan bilangan: '))
        if bilangan % 2 == 0:
            print ("%i adalah bilangan genap" % bilangan)
        else:
            print ("%i adalah bilangan ganjil" % bilangan)
        print(40*'=')
        pilihan = input('''Coba lagi [y/n]?
        ''')
        if pilihan == 'y':
            y = True
        elif pilihan == 'n':
            n = y = n
    # Cek jumlah huruf vokal        
    elif opsi == 4:
        print('==============================')
        print('Program cek jumlah huruf vokal')
        print('==============================')
        teks = input('Tuliskan teks: ').lower()
        x = teks.split()
        dictionary_huruf_vokal = {
                'a': 0,
                'i': 0,
                'u': 0,
                'e': 0,
                'o': 0
                }
        for huruf_vokal in dictionary_huruf_vokal.keys():
            dictionary_huruf_vokal[huruf_vokal] = teks.count(huruf_vokal)
            total_huruf_vokal = sum(dictionary_huruf_vokal.values())
        print(f'Jumlah huruf: {len(teks)}')
        print(f'Jumlah Kata: ',(len(x)))
        print(f'Jumlah huruf vokal: {total_huruf_vokal}')
        print(f"""\
        vokal a ada sebanyak {dictionary_huruf_vokal['a']}
        vokal i ada sebanyak {dictionary_huruf_vokal['i']}
        vokal u ada sebanyak {dictionary_huruf_vokal['u']}
        vokal e ada sebanyak {dictionary_huruf_vokal['e']}
        vokal o ada sebanyak {dictionary_huruf_vokal['o']}    
            """)
        print('==============================')
        pilihan = input('''Coba lagi [y/n]?
        ''')
        if pilihan == 'y':
            y = True
        elif pilihan == 'n':
            n = y = n
    elif opsi == 5:
        print('\n')
        print('==========================================')
        print('     Program Hitung Luas Lingkaran')
        print('==========================================')
        jari2= int(input('Masukkan Jari-jari: '))
        phi = 3.14
        lingkaran =phi * jari2 * jari2
        print('Luas Lingkaran: ',lingkaran)
        print('==========================================')
        pilihan = input('''Coba lagi [y/n]?
        ''')
        if pilihan == 'y':
            y = True
        elif pilihan == 'n':
            n = y = n        
    # out / kondisi false
    elif opsi == 6:
        y = n