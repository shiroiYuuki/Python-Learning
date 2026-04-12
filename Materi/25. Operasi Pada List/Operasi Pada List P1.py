## Operasi

# index(0(-3), 1(-2),2(-1))
data = ["Ucup", "Otong", "Dudung"]

# Mengambil data dari list ini
data0 = data[0]
print(f"data pertama (index 0) adalah {data0}\n")

dataTerakhir = data[-1]
print(f"data terakhir (index -1) adalah {dataTerakhir}\n")


dataUcup = data[-3]
print(f"data Ucup (index -3) adalah {dataUcup}\n")

# Mengambil info jumlah panjang data
panjangData = len(data)
print(f"panjang data adalah {panjangData}\n")

## Manipulasi data list

# Menambahkan item pada list sesuai posisi
print(f"data sebelum ditambah = \n{data}\n")

data.insert(1, "Asep") # menambahkan asep di index ke 1 
print(f"data setelah di tambahkan = \n{data}\n")

data.append("Jajang") # menambahkan jajang di paling belakang
print(f"data setelah di tambahkan lagi = \n{data}\n")

# Menambah list dengan list
dataBaru = ["Ujang", "Asep", "Dadang"]
data.extend(dataBaru) # menambah data baru di belakang(kalo ada data yang sama maka tidak di timpas)
print(f"data setelah di gabungkan lagi = \n{data}\n")

# Merubah data
# Kita ubah data 2 menjadi michael
data[2] = "Michael"
print(f"data setelah di ubah = \n{data}\n")

# Meremove/hapus data
data.remove("Ujang")
print(f"data setelah di hapus = \n{data}\n")
# data.remove("usep") akan error karena huruf harus sesuai yaitu "Usep"

# Meremove data paling belakang
dataAkhir = data.pop()
print(f"data akhir = \n{data}\n") # si "dadang" hilang

print(dataAkhir)