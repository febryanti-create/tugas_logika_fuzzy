print('NAMA : WA ODE IKA FEBRYANTI \nNIM : E1E120022 \n')
import sys
import numpy as np
import matplotlib.pyplot as plt
import math


print('Diketahui :')
print('Variabel linguistik : Permintaan, Persediaan, Produksi Barang')
print('Permintaan Terbesar = 5000 \nPermintaan Terkecil = 1000 \nPersediaan Terbanyak = 600 \nPersediaan Terkecil = 100')
print('Produksi Barang Berkurang = 7000 \nProduksi Barang Bertambah = 2000')

print('Pertanyaan : ')
permintaan = int(input('Masukkan  Jumlah Permintaan = '))
persediaan = int(input('Masukkan Jumlah Persediaan = '))

print('\n1. Fuzzyfikasi')
print('\nPermintaan {Naik, Turun}')
print('Persedian {Sedikit, Banyak}')
print('Produksi Barang {Bertambah, Berkurang}\n')

def permintaan_turun(permintaan):
    if permintaan <= 1000:
        return 1.0
    elif permintaan >= 5000:
        return 0.0
    else:
        return (5000 - permintaan) / (5000 - 1000)


def permintaan_naik(permintaan):
    if permintaan <= 1000:
        return 0.0
    elif permintaan >= 5000:
        return 1.0
    else:
        return (permintaan - 1000) / (5000 - 1000)

def persediaan_sedikit(persediaan):
    if persediaan <= 100:
        return 1.0
    elif persediaan >= 600:
        return 0.0
    else:
        return (600 - persediaan) / (600 - 100)


def persediaan_banyak(persediaan):
    if persediaan <= 100:
        return 0.0
    elif persediaan >= 600:
        return 1.0
    else:
        return (persediaan - 100) / (600 - 100)

def prod_brg_berkurang(produksi):
    if produksi <= 2000:
        return 1.0
    elif produksi >= 7000:
        return 0.0
    else:
        return (7000 - produksi) / (7000-2000)


def prod_brg_bertambah(produksi):
    if produksi <= 2000:
        return 0.0
    elif produksi >= 7000:
        return 1.0
    else:
        return (produksi - 2000) / (7000-2000)


# permintaan turun
print('Nilai derajat keanggotaan permintaan turun = ', permintaan_turun(permintaan))
x = np.linspace(0, 5000+50, 10000)
y = [permintaan_turun(i) for i in x]
plt.plot(x, y)
plt.xlabel('x')
plt.ylabel('Keanggotaan')
plt.title('Fungsi Keanggotaan Permintaan Turun')
if permintaan < 0 or permintaan > 10000:
    print("Nilai x harus antara 0 dan 10000")
else:
    y_input = permintaan_turun(permintaan)
    plt.plot(x, y)
    plt.xlabel('x')
    plt.axvline(x=permintaan, color='g', linestyle='--')
    plt.axhline(y=y_input, color='g', linestyle='--')


# permintaan naik
print('Nilai derajat keanggotaan permintaan naik = ', permintaan_naik(permintaan))
x = np.linspace(0, 5000+50, 10000)
y = [permintaan_naik(i) for i in x]
plt.plot(x, y)
plt.xlabel('x')
plt.ylabel('Keanggotaan')
plt.title('Fungsi Keanggotaan Permintaan Naik')
if permintaan < 0 or permintaan > 10000:
    print("Nilai x harus antara 0 dan 10000")
else:
    y_input = permintaan_naik(permintaan)
    plt.plot(x, y)
    plt.xlabel('x')
    plt.ylabel('Derajat Keanggotaan')
    plt.title('Fungsi Keanggotaan Permintaan Naik dan Turun')
    plt.axvline(x=permintaan, color='g', linestyle='--')
    plt.axhline(y=y_input, color='g', linestyle='--')
plt.show()


# persediaan sedikit
print('Nilai derajat keanggotaan persediaan turun = ', persediaan_sedikit(persediaan))
x = np.linspace(0, 600+50, 10000)
y = [persediaan_sedikit(i) for i in x]
plt.plot(x, y)
plt.xlabel('x')
plt.ylabel('Keanggotaan')
plt.title('Fungsi Keanggotaan Permintaan Turun')
if persediaan < 0 or persediaan > 10000:
    print("Nilai x harus antara 0 dan 10000")
else:
    y_input = persediaan_sedikit(persediaan)
    plt.plot(x, y)
    plt.xlabel('x')
    plt.axvline(x=persediaan, color='g', linestyle='--')
    plt.axhline(y=y_input, color='g', linestyle='--')


# persediaan banyak
print('Nilai derajat keanggotaan persediaan naik = ', persediaan_banyak(persediaan))
x = np.linspace(0, 600+50, 10000)
y = [persediaan_banyak(i) for i in x]
plt.plot(x, y)
plt.xlabel('x')
plt.ylabel('Keanggotaan')
plt.title('Fungsi Keanggotaan Permintaan Naik')
if persediaan < 0 or persediaan > 10000:
    print("Nilai x harus antara 0 dan 10000")
else:
    y_input = persediaan_banyak(persediaan)
    plt.plot(x, y)
    plt.xlabel('x')
    plt.ylabel('Derajat Keanggotaan')
    plt.title('Fungsi Keanggotaan Persediaan Terkecil dan Terbanyak')
    plt.axvline(x=persediaan, color='g', linestyle='--')
    plt.axhline(y=y_input, color='g', linestyle='--')
plt.show()


# Produksi barang berkurang
x = np.linspace(0, 7000+50, 10000)
y = [prod_brg_berkurang(i) for i in x]
plt.plot(x, y)
plt.xlabel('x')
plt.plot(x, y)

# Produksi barang bertambah
x = np.linspace(0, 7000+50, 10000)
y = [prod_brg_bertambah(i) for i in x]
plt.plot(x, y)
plt.xlabel('x')
plt.ylabel('Derajat Keanggotaan')
plt.title('Fungsi Keanggotaan Produksi Barang Turun dan Naik')
plt.plot(x, y)
plt.show()


print('\n2. Operasi Logika Fuzzy dan')
print('3. Implikasi Kaidah Fuzzy')
print('[R1] IF Permintaan TURUN And Persediaan BANYAK THEN Produksi Barang BERKURANG')
nilai_min1 = min(permintaan_turun(permintaan), persediaan_banyak(persediaan))
print('(', '', permintaan_turun(permintaan), ',', '', persediaan_banyak(persediaan), ')')
print("Nilai minimum adalah", nilai_min1)

print('\n[R2] IF Permintaan TURUN And Persediaan SEDIKIT THEN Produksi Barang BERKURANG')
nilai_min2 = min(permintaan_turun(permintaan), persediaan_sedikit(persediaan))
print('(', '', permintaan_turun(permintaan), ',', '', persediaan_sedikit(persediaan), ')')
print("Nilai minimum adalah", nilai_min2)
print('\n[R3] IF Permintaan NAIK And Persediaan BANYAK THEN Produksi Barang BERTAMBAH')
nilai_min3 = min(permintaan_naik(permintaan), persediaan_banyak(persediaan))
print('(', '', permintaan_naik(permintaan), ',', '', persediaan_banyak(persediaan), ')')
print("Nilai minimum adalah", nilai_min3)
print('\n[R4] IF Permintaan NAIK And Persediaan SEDIKIT THEN Produksi Barang BERTAMBAH')
nilai_min4 = min(permintaan_naik(permintaan), persediaan_sedikit(persediaan))
print('(', '', permintaan_naik(permintaan), ',', '', persediaan_sedikit(persediaan), ')')
print("Nilai minimum adalah", nilai_min4)

print('\n4. Agregasi\n')
print('(', '', nilai_min1, ',', '', nilai_min2, ')\n')
nilai_max1 = max(nilai_min1, nilai_min2)
print("Nilai Maximum adalah", nilai_max1)
print("\n")
print('(', '', nilai_min3, ',', '', nilai_min4, ')\n')
nilai_max2 = max(nilai_min3, nilai_min4)
print("Nilai Maximum adalah", nilai_max2,"\n")

if nilai_max1 > nilai_max2:
    z1 = 7000 - (5000*nilai_max1)
    print("Nilai a1 adalah ", z1)
    z2 = 7000 - (5000*nilai_max2)
    print("Nilai a2 adalah ", z2)

    print("\n \nFungsi baru yang terbentuk adalah: ")
    print("\n ", nilai_max1, " ; z <= ", z1)
    print("7000-z/5000", " ; ", z1, "<=z<=", z2)
    print(" ", nilai_max2, " ; >= ", z2,"\n")

else:
    z1 = (5000*nilai_max1)+2000
    print("Nilai a1 adalah ", z1)
    z2 = (5000*nilai_max2)+2000
    print("Nilai a2 adalah ", z2)

    print("\n \nFungsi baru yang terbentuk adalah: ")
    print("\n ", nilai_max1, " ; z<= ", z1)
    print("z-2000/5000", " ; ", z1, "<=z<=", z2)
    print(" ", nilai_max2, " ; >= ", z2,"\n")