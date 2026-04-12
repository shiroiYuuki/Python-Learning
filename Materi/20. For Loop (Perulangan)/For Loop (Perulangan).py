# Perulangan (Loop)

# for kondisi in var:
#   aksi

# 1. Ini dengan list
angka1_list = [0,2,4,8,10]
print(angka1_list)

for i in angka1_list:
    print(f"i sekarang adalah {i}") # akan memprint keseluruhan

print("ini adalah akhir dari program 1\n")

# 2. ini dengan range
angka2_range1 = range(5)
for i in angka2_range1:
    print(f"i sekarang adalah {i}") # akan memprint 0 - 4
print("ini adalah akhir dari program 2\n")

angka2_range2 = range(1,10)
for x in angka2_range2: 
    print(f"x sekarang adalah {x}") # akan memprint 1 - 9
    print("anjay keren")
print("ini adalah akhir dari program 3\n")

# 3. ini dengan string
dataStr = "saya keren banget"
for i in dataStr:
    print(i) # akan memprint perhuruf
print("ini adalah akhir dari program 4\n")

# 4. ngeprint sesuai jumlah huruf
dataJumlah = "saya" # (4)
for i in dataJumlah:
    print(dataJumlah) # akan memprint sesuai jumlah huruf
print("ini adalah akhir dari program 5\n")