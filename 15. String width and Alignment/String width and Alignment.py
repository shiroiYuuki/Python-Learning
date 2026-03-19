# Width and Multiline

# Data

dataNama = "Ucup Surucup"
dataUmur = 17
dataTinggi = 150.1
dataNomorSepatu = 44

# String standard
dataString = f"Nama = {dataNama}, \nUmur = {dataUmur}, \nTinggi = {dataTinggi}, \nSepatu = {dataNomorSepatu}"
print(5*"="+"Data String 1"+5*"=")
print(dataString)

# String Multiline(kutip triplet)
dataString = f"""Nama = {dataNama}
Umur = {dataUmur},
Tinggi = {dataTinggi},
Sepatu = {dataNomorSepatu}"""

print(5*"="+"Data String 2"+5*"=")
print(dataString)

# Mengatur lebar

dataString = f"""Nama = {dataNama:>5}
Umur = {dataUmur:>5}
Tinggi = {dataTinggi:>5}
Sepatu = {dataNomorSepatu:>5}
""" # jika datanya lebih dari 5 maka akan kesamping

print(5*"="+"Data String 2"+5*"=")
print(dataString)



