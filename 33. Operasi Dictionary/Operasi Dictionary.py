# Operator Dictionary


dataDict = {
    "cup":"Ucup surucup",
    "tong":"Otong surotong",
    "dung":"Dududng surudung"
}

# Panjang Dictionary
lendict = len(dataDict) # untuk menghitung jumlah data yang ada di dalam
print(f"Panjang dictionary: {lendict}\n")

# Mengecek key exist atau tidak
key = "cup"
checkKey = key in dataDict
print(f"apakah {key} ada di dataDict: {checkKey}\n")

# Mengakses  value(Read) dengan get
print(dataDict["cup"])
print(dataDict.get("cup")) # untuk mengetahui yang di ambil adalah Dict
print(dataDict.get("kis")) # jika tidak ada otomatis "None"
print(dataDict.get("cik","Key tidak ditemukan\n")) # pesan "None"-nya bisa di ubah 

# Mengupdate data
dataDict["cup"] = "ucup si ganteng" # cara memodifikasi dictionary
print(dataDict)
dataDict["sep"] = "asep si kasyep"
print(dataDict,"\n")

# Update 1 Data (key, items)
dataDict.update({"cup":"surucup"}) # untuk update 1 data penuh
print(dataDict)
dataDict.update({"budi":"cecep terbang"})
print(dataDict)

# Mendelete data pada dict
del dataDict["budi"] # untuk delete 1 data
print(dataDict)