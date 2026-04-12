## List

# Kumpulan data numbers
dataAngka = [1,2,4,2]
print(dataAngka)

# Kumpulan data string
dataString = ["ucup", "otong", "budi"]
print(dataString)

# Kumpulan data boolean
dataBoolean = [True, False, True, False]
print(dataBoolean)

# Kumpulan data campuran
dataCampuran = [1, "udin", True, "cecep", 4, False]
print(dataCampuran)

## Cara alternatif membuat list
dataAlternatif = range(0,10,2) # range(start, stop, step)
print(dataAlternatif)
dataList = list(dataAlternatif)
print(dataList)

# Membuat list dengan for loop, list Comprehesion
listPakeFor1 = [i for i in range(0,10)]
listPakeFor2 = [i**2 for i in range(0,10)] # di kuadrat 2
print(listPakeFor1)
print(listPakeFor2)

# Membuat list pake for pake if
listPakeForIf = [i for i in range(0,10) if i != 5] # mengkecualikan angka 5
print(listPakeForIf)

listPakeForIf = [i for i in range(0,10) if i%2 == 0] # mengkecualikan Ganjil
print(listPakeForIf)

listPakeForIf = [i for i in range(0,10) if i%2 != 0] # mengkecualikan Genap
print(listPakeForIf)