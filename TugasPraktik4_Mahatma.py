nis = input("Masukkan Nis = ")
nama = input ("Masukkan Nama = ")
mapel = input ("Masukkan Mata pelajaran =")
absensi = int (input ("Masukkan nilai absensi = "))
tugas = int (input ("Masukkan nilai tugas = "))
uts = int (input ("Masukkan nilai uts = "))
uas = int (input("Masukkan nilai uas = "))
nilai = 0.20 * absensi + 0.25 * tugas + 0.25 * uts + 0.30 * uas
print(53*"=")
print("  Program Hitung Nilai Mata Pelajaran Dengan Python")
print(53*"=")
print("NIS = ",nis)
print("Nama = ",nama)
print("Mata pelajaran = ",mapel)
print("Nilai Akhir = ",nilai)
if nilai >= 90:
    rank = "A"
    ket= "Sangat baik"
elif nilai >= 80:
    rank = "b"
    ket = "baik" 
elif nilai >= 70:
    rank = "c"
    ket = "kurang"
print("Grade = %s" % rank)
print("Keterangan = %s" % ket )
print(53*"=")