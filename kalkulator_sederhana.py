while ( True ) :
    kalkulator = input("""
===Kalkulator Sederhana===    
1. penjumlahan
2. pengurangan
3. perkalian
4. pembagian
masukkan pilihan anda: """)
    while (kalkulator != '1' and kalkulator != '2' and kalkulator != '3' and kalkulator != '4'):
        kalkulator = input("""\nmaaf inputan anda salah. Silahkan coba lagi. \n
===Kalkulator Sederhana===
1. penjumlahan
2. pengurangan
3. perkalian
4. pembagian
masukkan pilihan anda: """)
    if kalkulator == '1' :
        print("\n===Penjumlahan Sederhana===")
        a = int(input("masukkan angka pertama: " ))
        b = int(input("masukkan angka kedua: "))
        hasil = a + b 
        print (a,"+",b,"= ",hasil)
        ulang = input ("kembali?[y/n] : ")
        while (ulang != 'y' and ulang != 'n') :
            ulang = input ("maaf inputan anda salah. silahkan coba lagi\nkembali?[y/n]: ")
        if ulang == "y" :
             print("\nSilahkan.\n")
        elif ulang == "n" :
            print("\nTerimakasih.\n")
            break
    elif kalkulator == '2' :
        print("\n===Pengurangan Sederhana===")
        a = int(input("masukkan angka pertama: " ))
        b = int(input("masukkan angka kedua: "))
        hasil = a - b 
        print (a,"-",b,"= ",hasil)
        ulang = input ("kembali?[y/n] : ")
        while (ulang != 'y' and ulang != 'n') :
            ulang = input ("maaf inputan anda salah. silahkan coba lagi\nkembali?[y/n]: ")
        if ulang == "y" :
             print("\nSilahkan.\n")
        elif ulang == "n" :
            print("\nTerimakasih.\n")
            break
    elif kalkulator == '3' :
        print("\n===Perkalian Sederhana===")
        a = int(input("masukkan angka pertama: " ))
        b = int(input("masukkan angka kedua: "))
        hasil = a * b 
        print (a,"x",b,"= ",hasil)
        ulang = input ("kembali?[y/n] : ")
        while (ulang != 'y' and ulang != 'n') :
            ulang = input ("maaf inputan anda salah. silahkan coba lagi\nkembali?[y/n]: ")
        if ulang == "y" :
             print("\nSilahkan.\n")
        elif ulang == "n" :
            print("\nTerimakasih.\n")
            break
    elif kalkulator == '4' :
        print("\n===Pembagian Sederhana===")
        a = int(input("masukkan angka pertama: " ))
        b = int(input("masukkan angka kedua: "))
        hasil = a / b 
        print (a,":",b,"= ",hasil)    
        ulang = input ("kembali?[y/n] : ")
        while (ulang != 'y' and ulang != 'n') :
            ulang = input ("maaf inputan anda salah. silahkan coba lagi\nkembali?[y/n]: ")
        if ulang == "y" :
             print("\nSilahkan.\n")
        elif ulang == "n" :
            print("\nTerimakasih.\n")
            break