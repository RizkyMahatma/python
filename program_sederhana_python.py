while (True):
    opsi = input(  '''
==========================================
Selamat Datang di Program Sederhana Python
==========================================
1. Persegi Panjang
2. Rata-rata Nilai
3. Cek Bilangan Ganjil Atau Genap
4. Jumlah Huruf Vokal
5. Keluar
Masukkan Pilihan kamu: ''')
    while (opsi != '1' and opsi != '2' and opsi != '3' and opsi != '4' and opsi != '5'):
        opsi = input( ''' \nInput yang dimasukkan salah. Coba Lagi.
\n==========================================
Selamat Datang di Program Sederhana Python
==========================================
1. Persegi Panjang
2. Rata-rata Nilai
3. Cek Bilangan Ganjil Atau Genap
4. Jumlah Huruf Vokal
5. Keluar
Masukkan Pilihan kamu: ''')
    # Rumus Persegi Panjang
    if opsi == '1':
        print('\n')
        print(51*'=')
        print('Program Hitung luas dan keliling persegi panjang')
        print(51*'=')
        panjang = int(input('Masukkan Panjang: ' ))
        lebar = int(input('Masukkan Lebar: '))
        print('\n')
        print(31*'=')
        print('Hasil Perhitungan dengan Python')
        print(31*'=')
        hasil = panjang * lebar
        hasil1 = 2 * (panjang + lebar)
        luas = print('Luas persegi panjang adalah: ',hasil,'CM')
        keliling = print('Keliling persegi panjang adalah: ',hasil1,'CM')
        print(31*'=')
        ulang = input ("kembali?[y/n] : ")
        while (ulang != 'y' and ulang != 'n') :
            ulang = input ("maaf inputan anda salah. silahkan coba lagi\nkembali?[y/n]: ")
        if ulang == "y" :
             print("\nSilahkan.\n")
        elif ulang == "n" :
            print("\nTerimakasih.\n")
            break

    # Menghitung Nilai Rata rata
    elif opsi == '2':
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
        ulang = input ("kembali?[y/n] : ")
        while (ulang != 'y' and ulang != 'n') :
            ulang = input ("maaf inputan anda salah. silahkan coba lagi\nkembali?[y/n]: ")
        if ulang == "y" :
             print("\nSilahkan.\n")
        elif ulang == "n" :
            print("\nTerimakasih.\n")
            break
    # cek bilangan ganjil/genap        
    elif opsi == '3':
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
        ulang = input ("kembali?[y/n] : ")
        while (ulang != 'y' and ulang != 'n') :
            ulang = input ("maaf inputan anda salah. silahkan coba lagi\nkembali?[y/n]: ")
        if ulang == "y" :
             print("\nSilahkan.\n")
        elif ulang == "n" :
            print("\nTerimakasih.\n")
            break
    # Cek jumlah huruf vokal        
    elif opsi == '4':
        print('==============================')
        print('Program cek jumlah huruf vokal')
        print('==============================')
        teks = input('Tuliskan teks: ').lower()
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
        print(f'Jumlah huruf vokal: {total_huruf_vokal}')
        print(f"""\
        vokal a ada sebanyak {dictionary_huruf_vokal['a']}
        vokal i ada sebanyak {dictionary_huruf_vokal['i']}
        vokal u ada sebanyak {dictionary_huruf_vokal['u']}
        vokal e ada sebanyak {dictionary_huruf_vokal['e']}
        vokal o ada sebanyak {dictionary_huruf_vokal['o']}    
            """)
        print('==============================')
        ulang = input ("kembali?[y/n] : ")
        while (ulang != 'y' and ulang != 'n') :
            ulang = input ("maaf inputan anda salah. silahkan coba lagi\nkembali?[y/n]: ")
        if ulang == "y" :
             print("\nSilahkan.\n")
        elif ulang == "n" :
            print("\nTerimakasih.\n")
            break
    # out / kondisi false
    elif opsi == '5':
        break