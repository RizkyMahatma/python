def luas_segiempat(x0,y0,x1,y1):
# Menghitung Luas Segi empat berdasarkan koordinat 2 titik: pojok kiri bawah (x0, y0), dan kanan atas (x1,y1).
    

    # cek (x0,y0) kiri bawah, dan (x1,y1) kanan atas
    if x0 < x1 and y0 < y1:
        deltax = x1 - x0 
        deltay = y1 - y0
        return deltax * deltay
    
segi4_1 = luas_segiempat(1,1,3,3)
segi4_2 = luas_segiempat(2,4,3,3)
print(segi4_1 + segi4_2)