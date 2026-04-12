data0 = [1, 2]
data1 = [3, 4, 5]

dataListBiasa = [1,2,3,4]


print(f"List biasa = {dataListBiasa}\n")

list2D = [data0, data1, 6, 7]
print(f"List 2D = {list2D}\n")

# Contoh penggunaan
peserta0 = ["Ucup", 25, "Laki-Laki"]
peserta1 = ["Otong", 10, "Laki-Laki"]
peserta2 = ["dedeh", 50, "Perempuan\n"]

listPeserta = [peserta0, peserta1, peserta2]
print(f"Peserta = {listPeserta}\n")

for peserta in listPeserta:
    print(f"Nama\t: {peserta[0]}")
    print(f"Umur\t: {peserta[1]}")
    print(f"Gender\t: {peserta[2]}\n")

# Dengan reference
listCopy = listPeserta.copy()
print(f"Peserta = {listCopy}")
peserta0[0] = "Michael"
print(f"Peserta = {listCopy}") # akan berubah keduanya karena mereka berbagi satu address yang sama
print(f"Peserta = {listPeserta}")
