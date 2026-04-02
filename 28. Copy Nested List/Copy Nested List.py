data0 = [1,2]
data1 = [3,4]

data2D = [data0, data1, 10]
data2DCopy = data2D.copy()

print(f"Data = {data2D}")
print(f"Data copy = {data2DCopy}")

# Mengambil data dari nested list

# Baris ke 2 urutan yang ke 1
data = data2D[1][0]
print(f"data a= {data}")

# Address Semuanya
print(f"Address asli = {hex(id(data2D))}") #(1) listnya berbeda addressnya
print(f"Address copy = {hex(id(data2DCopy))}")

print("Address dari member ke-1")
print(f"Address asli = {hex(id(data2D[0]))}") #(2) tapi isinya memiliki address yang berbeda
print(f"Address copy = {hex(id(data2DCopy[0]))}")

data2D[1][0] = 5
data2D[2] = 9
print(f"Data = {data2D}")
print(f"Data copy = {data2DCopy}")



# kita gunakan deepcopy

from copy import deepcopy
data2D = [data0, data1, 10]
data2DeepCopy = deepcopy(data2D)

print(f"Address asli = {hex(id(data2D))}")
print(f"Address copy = {hex(id(data2DCopy))}")

print("Address dari member ke-1")
print(f"Address asli = {hex(id(data2D[0]))}")
print(f"Address copy = {hex(id(data2DCopy[0]))}")

data2D[1][0] = 30
print(f"Data = {data2D}") # ini akan berubah
print(f"Data copy = {data2DCopy}") # ini akan berubah
print(f"Data deepcopy = {data2DeepCopy}") # data ini tidak akan berubah