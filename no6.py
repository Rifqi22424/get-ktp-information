def hitungKeliling_dan_hitungLuas(p,l):
    keliling = 2 * (p + l)
    luas = p * l
    return [keliling, luas]

p = 5
l = 3
hasil = hitungKeliling_dan_hitungLuas(p,l)
print(hasil)