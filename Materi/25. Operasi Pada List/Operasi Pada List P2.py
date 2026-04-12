dataAngka = [1,2,5,3,7,2,9,1,7,4,0,4,2,2]

print(f"data angka = {dataAngka}\n")

# Count data

jumlahData4 = dataAngka.count(4)
jumlahData2 = dataAngka.count(2) # menghitung jumlah angka 2 dalam list tsb.

print(f"Jumlah angka 4 adalah {jumlahData4}") 
print(f"Jumlah angka 2 adalah {jumlahData2}\n")

# Ambil posisi data(index)

data = ["Ucup", "Otong", "Dudung", "Ujang"]
print(f"data = {data}\n")

indexDudung = data.index("Dudung")
indexUjang = data.index("Ujang")
print(f"index si Dudung adalah {indexDudung}") # mencari tau index "Dudung"
print(f"index si Ujang adalah {indexUjang}\n")

# Mengurutkan list
print(f"data angka sebelum di sort = \n{dataAngka}")
dataAngka.sort() # untuk mengurutkan di list
print(f"data angka sesudah di sort = \n{dataAngka}\n")

print(f"data = {data}")
data.sort() # bisa juga untuk string(mengikuti abjad)
print(f"data = {data}\n")

# balik isinya
dataAngka.reverse() # data harus di urutkan terlebih dahulu
data.reverse() # agar hasilnya rapi
print(f"data di reverse = \n{dataAngka} \n{data}")