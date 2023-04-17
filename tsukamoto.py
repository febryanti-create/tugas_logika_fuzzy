print('NAMA : WA ODE IKA FEBRYANTI \nNIM : E1E120022 \n')

import numpy as np
import matplotlib.pyplot as plt



print('Diketahui :')
print('Variabel linguistik : Permintaan, Persediaan, Produksi Barang')
print('Permintaan Terbesar = 5000 \nPermintaan Terkecil = 1000 \nPersediaan Terbanyak = 600 \nPersediaan Terkecil = 100')


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



print('\nnilai a-predikat dan Z setiap aturan')

print('\n2[R1] IF Permintaan TURUN And Persediaan BANYAK THEN Produksi Barang BERKURANG')
nilai_min1 = min(permintaan_turun(permintaan), persediaan_banyak(persediaan))
print('min(', permintaan_turun(permintaan), ',', '', persediaan_banyak(persediaan), ')')
print("Nilai a-predikat1 =", nilai_min1)

nilai_z1 = 7000 -  (nilai_min1 * 5000)
print('\n PRODUKSI BARANG BERKURANG')
print('Nilai Z1 =', nilai_z1)

print('\n[R2] IF Permintaan TURUN And Persediaan SEDIKIT THEN Produksi Barang BERKURANG\n')
nilai_min2 = min(permintaan_turun(permintaan), persediaan_sedikit(persediaan))
print('min(', permintaan_turun(permintaan), ',', '', persediaan_sedikit(persediaan), ')')
print("Nilai a-predikat2 =", nilai_min2)

nilai_z2 = 7000 -  (nilai_min2 * 5000)
print('\nPRODUKSI BARANG BERKURANG')
print('Nilai Z2 =', nilai_z2)

print('\n[R3] IF Permintaan NAIK And Persediaan BANYAK THEN Produksi Barang BERTAMBAH\n')
nilai_min3 = min(permintaan_naik(permintaan), persediaan_banyak(persediaan))
print('min(', permintaan_naik(permintaan), ',', '', persediaan_banyak(persediaan), ')')
print("Nilai a-predikat3 =", nilai_min3)

nilai_z3 = (nilai_min3 * 5000) + 2000
print('\nPRODUKSI BARANG BERTAMBAH')
print('Nilai Z3 =', nilai_z3)

print('\n[R4] IF Permintaan NAIK And Persediaan SEDIKIT THEN Produksi Barang BERTAMBAH\n')
nilai_min4 = min(permintaan_naik(permintaan), persediaan_sedikit(persediaan))
print('min(', permintaan_naik(permintaan), ',', '', persediaan_sedikit(persediaan), ')')
print("Nilai a-predikat4 =", nilai_min4)

nilai_z4 = (nilai_min4 * 5000) + 2000
print('\nPRODUKSI BARANG BERTAMBAH')
print('Nilai Z4 =', nilai_z4)

z = ((nilai_min1 * nilai_z1) + (nilai_min2 * nilai_z2) + (nilai_min3 * nilai_z3) + (nilai_min4 * nilai_z4))/(nilai_min1 + nilai_min2 + nilai_min3 + nilai_min4)
print('\nJadi, jumlah makanan jenis ABC yang harus diproduksi sebanyak ', round(z))