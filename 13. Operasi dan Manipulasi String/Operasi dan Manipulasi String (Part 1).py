# Operasi dan Memanipulasi String

# 1. Menyambung string (concatenate)
namaPertama = "Ucup"
namaTengah = "D"
namaAkhir = "Fame"


namaLengkap = namaPertama + namaTengah + namaAkhir
print(namaLengkap)

namaLengkap = namaPertama + " " + namaTengah + "'" + namaAkhir
print(namaLengkap)

# 2. Menghitung panjang string
panjang = len(namaLengkap) # menghitung jumlah panjang string tsb
print("panjang " + namaLengkap + " adalah " + str(panjang))

# 3. Operator untuk string

# cek apakah ada komponen pada sebuah string

d = "d"
status = d in namaLengkap
print("apakah " + d + " ada di " + namaLengkap + ", " + str(status))

D = "D"
status = D in namaLengkap
print("apakah " + D + " ada di " + namaLengkap + ", " + str(status))

x = "x"
status = x in namaLengkap
print("apakah " + x + " ada di " + namaLengkap + ", " + str(status))

# mengulang string 
print("wk"*10) # mengulang string 10x
print(100*"wk") # mengulang string 10x

# indexing
print("index ke-0 : " + namaLengkap[0]) # dimulai dari 0
print("index ke-6 : " + namaLengkap[6]) # index bebas
print("index ke-(-1) : " + namaLengkap[-1]) # indexing dari dibelakang
print("index ke-(6,8) : " + namaLengkap[6:8]) # dimulai dari index 6 sampai sebelum 8
print("index ke-[0,2,4,6,8] : " + namaLengkap[0:10:2]) # dimulai dari index 6 sampai sebelum 8

# item paling kecil
print("nilai terkecil : " + min(namaLengkap))
print("nilai terbesar : " + max(namaLengkap))

asciiCode = ord(" ")
print("ASCII number dari spasi : " + str(asciiCode))
data = 117
print("Character dari ascii code 117 : " + chr(data))

# 4. Operator dalam bentuk method
data = "otong surotong pararotong"
jumlah = data.count("o") # menghitung jumlah 'o'
print("jumlah o di " + data + " : " + str(jumlah))


