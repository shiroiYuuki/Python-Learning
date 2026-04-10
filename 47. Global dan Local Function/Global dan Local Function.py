## Global dan Local scope

nama_global = "otong" # <- ini var global

# akses var global dalam fungsi
def fungsi1():
    print(f"fungsi menampilkan {nama_global}")

fungsi1()

# akses var global dalam loop
for i in range(0,5):
    print(f"loop {i} - {nama_global}")

# percabangan
if True:
    print(f"if menampilkan {nama_global}")


## Var Local Scope

def fungsi2():
    nama_local = "Ucup" # <- var lokal scope

fungsi2()
# print(nama_local) # tidak bisa dilakukan

## Contoh 1: penggunaan akses variabel
def say_otong():
    print(f"Hello {nama}")

nama = "Otong"
say_otong()

## contoh 2: merubah variabel global
angka = 0
name = "Ucup"

def ubah(nilai_baru, nama_baru):
    global angka # fungsi ini mendapat akses merubah angka
    global name
    angka = nilai_baru
    name = nama_baru

print(f"Sebelum {angka,name}")
ubah(10,"Otong")
print(f"Sesudah {angka,name}")

## contoh 3:
angka = 0

for i in range(0,5):
    angka += i
    angka_dummy = 0

print(angka)
print(angka_dummy)

if True:
    angka = 5
    angka_dummy = 10

print(angka)
print(angka_dummy)