# Lambda function

def f_kuadrat(angka):
    return angka**2

print(f"hasil fungsi kuadrat = {f_kuadrat(3)}")

# coba dengan lambda
# output = lambda argument: expression
kuadrat = lambda angka : angka**2
print(f"hasil fungsi kuadrat = {kuadrat(5)}")

pangkat = lambda num,pow : num**pow
print(f"hasil fungsi kuadrat = {pangkat(4,2)}")

# kegunaan

# sorting untuk list biasa
dataList = ["Otong", "Ucup", "Dudung"]
dataList.sort()
print(f"sorted list = {dataList}")
print(f"sorted list = {dataList}")

# sorting data pakai panjang
def panjangNama(nama):
    return len(nama)

dataList.sort(key=panjangNama)
print(f"sorted list by panjang = {dataList}")

# sort pakai lambda
dataList = ["Otong", "Ucup", "Dudung"]
dataList.sort(key=lambda nama:len(nama))
print(f"sorted list by lambda = {dataList}")

# filter
dataAngka = [1,2,3,4,5,6,7,8,9,10,11,12]

def kurangDariLima(angka):
    return angka < 5

dataAngkaBaru = list(filter(kurangDariLima, dataAngka))
dataAngkaBaru = list(filter(lambda x:x<7, dataAngka))
print(dataAngkaBaru)

# kasus genap
dataGenap = list(filter(lambda x:(x%2==0), dataAngka))
print(dataGenap)

# kasus ganjil
dataGanjil = list(filter(lambda x:(x%2!=0), dataAngka))
print(dataGanjil)

# kelipatan 3
data3 = list(filter(lambda x:(x%3==0), dataAngka))
print(data3)

# anonymous function
# currying <- Curry

def pangkat(angka,n):
    hasil = angka**n
    return hasil

dataHasil = pangkat(5,2)
print(f"fungsi biasa {dataHasil}")

# dengan currying menjadi

def pangkat(n):
    return lambda angka:angka**n

pangkat2 = pangkat(2)
print(f"pangkat2 = {pangkat2(5)}")
pangkat3 = pangkat(3)
print(f"pangkat3 = {pangkat3(3)}")
print(f"pangkat bebas = {pangkat(4)(5)}")