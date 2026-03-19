# Continue, pass

# Pass -> berfungsi sebagai dummy, tidak akan dieksekusi

# Pass
angka = 0
while angka < 5:
    angka += 1

    if angka == 3:
        pass # ini tidak akan dieksekusi

    print(f"angka sekarang adalah {angka}")

print(f"\n")
# Continue
angka = 0
print(f"Angka sekarang adalah -> {angka}")

while angka < 5:
    angka += 1
    print(f"Angka sekarang adalah -> {angka}") # aksi 1
    if angka == 3:
        print("Nice!") # Wassaup tidak akan di keluarkan jika ini keluar
        continue # akan membuat loop meloncat ke step Awal
    print("Wassaup!")
print("Finish!")