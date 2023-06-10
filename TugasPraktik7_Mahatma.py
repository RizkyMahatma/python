kondisi = True
kondisif = False
dataSiswa = []

while kondisi:
    pilihan = int(input('''
 ========================
    Program Data Siswa
 ========================             
1. Masukan data siswa
2. Tampilkan data siswa
3. Hapus data siswa
0. Keluar
 ========================
Masukkan pilihan kamu: '''))

    if pilihan == 1:
        input_NIS = input('\nMasukkan NIS\t: ')
        input_Nama = input('Masukkan Nama\t: ')
        input_Asal = input('Masukkan Asal\t: ')
        dataSiswa.append({
        'nama' : input_Nama, 
        'NIS' : input_NIS,
        'Asal' : input_Asal})

    elif pilihan == 2:
        print('\n')
        print(28*"=")
        print("NIS","\t","Nama","\t","Asal")
        print(28*"=")
        for siswa in dataSiswa:
            
            print(siswa['NIS'],'\t',siswa['nama'], '\t',siswa['Asal'])

    elif pilihan == 3:
        print('\n')
        for siswa in  dataSiswa:

            del dataSiswa[int(callable(input('\nHapus  NIS: '))) - 1]
            break
        
        
    elif pilihan == 0:
        kondisi = kondisif