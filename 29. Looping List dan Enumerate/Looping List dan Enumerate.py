# Looping dari list

# for loop
print("For loop")
kumpulanAngka = [4,3,2,5,2,5,6]
for angka in kumpulanAngka:
    print(f"angka = {angka}")
    
peserta = {"ucup", "otong", "dadang", "diding", "dudung"}

for nama in peserta:
    print(f"Nama peserta = {nama}")

# for loop and range
print("For loop and range\n")
kumpulanAngka = [10,9,3,1,4,2]

panjang = len(kumpulanAngka)

for i in range(panjang):
    print(f"angka = {kumpulanAngka[i]}")

# while loop
print("while loop")
kumpulanAngka = [10,9,3,1,4,2]
panjang = len(kumpulanAngka)
i = 0

while i < panjang:
    print(f"angka = {kumpulanAngka[i]}")
    i += 1
    
# list comprehension
print("\nlist comprehension")
data = ["Ucup", 1,2,3,"Otong"]

[print(f"data = {i}") for i in data]

kumpulanAngka = [10,9,3,1,4,2]
angkaKuadrat  =[i**2 for i in kumpulanAngka]
print(angkaKuadrat)

# enumerate
print("\nEnumerate")
dataList = ["Ucup", 1,2,3,"Otong"]

for index,data in enumerate(dataList):
    print(f"Index = {index}, data = {data}")