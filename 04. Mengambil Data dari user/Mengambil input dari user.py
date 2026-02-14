#Input dari user

data = input("Masukkan data: ") # data yang di masukkan pasti string

print("data = ", data, ", type =", type(data))

# jika kita ingin mengambil integer

angka = float(input("masukkan angka: "))
print("data = ", angka, ", type =", type(angka))

angka = int(input("masukkan angka: "))
print("data = ", angka, ", type =", type(angka))

# bagaimana dengan boolean
biner = bool(int(input("Masukkan nilai boolean: "))) # kalau ingin boolean maka harus ubah dulu ke int baru ke boolean

print("data = ", biner, ", type =", type(biner))