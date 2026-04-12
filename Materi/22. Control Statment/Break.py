# Break

angka = 0
while angka < 5:
    angka += 1
    print(f"Angka sekarang adalah: {angka}")
    if angka == 3:
        print("Keren")
        break
    print("Sup!")

print("Cukup.")

dataInt = int(input("Hitung sampai = "))

angka = 0
while True:
    angka += 1
    print(f"Count = {angka}")
    if angka == dataInt:
        print(f"Angka telah menyampai {dataInt}")
        break
    print("Sup!")

print("Finish, akhir dari code.")