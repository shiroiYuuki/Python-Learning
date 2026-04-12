# Program meminta:
#   nama user
#   umur user
# Sistem punya aturan:
#    umur < 13 → “Akses ditolak”
#    umur 13–17 → “Akses terbatas”
#    umur ≥ 18 → “Akses penuh”
# Tambahan logika:
#    nama kosong → tampilkan error
#    umur negatif → tampilkan error

import sys

print("=" * 5, "Mengecek Umur", "=" * 5)

nama = input("Masukkan nama anda: ")
if not nama.strip():
    print("Error: harus ada input(tidak termasuk spasi)")
    sys.exit(1)

try:
    umur = int(input("Masukkan umur anda: "))
except ValueError:
    print("\n Error, anda harus masukkan angka")
    print("Program akan keluar...")
    sys.exit(1)

if umur < 0:
    print("Maaf kami tidak menerima umur minus")
    sys.exit(1)

if umur < 13:
    print("Maaf Akses ditolak karena umur anda di bawah 13")
elif umur <= 17:
    print("Anda berhasil masuk, tapi Akses terbatas")
else:
    print("Anda berhasil masuk, Akses penuh")
