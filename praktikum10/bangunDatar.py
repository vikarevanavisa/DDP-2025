import math

def Persegi(sisi):
    hasil = math.pow (sisi, 2)
    return hasil
def PersegiPanjang(panjang, lebar):
    hasil = panjang * lebar
    return hasil
def Segitiga(alas, tinggi):
    hasil = 0.5 * alas * tinggi 
    return hasil
def Lingkaran(jari_jari):
    hasil = math.pi * math.pow (jari_jari, 2)
    return hasil 
def JajarGanjar(alas, tinggi):
    return alas * tinggi

print(Lingkaran(2))
