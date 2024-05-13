def cek_palindrom(kata):
    return kata == kata[::-1]

kata = "level"
hasil = cek_palindrom(kata)
print(hasil)