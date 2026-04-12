# List -> array, mengakses dengan
# menggunakan index

dataList = ["Ucup", "Otong", "Dudung"]
print(dataList[0])

# Dictionary(dict) -> associative array
# identifier -> key

dataDict = {
    "Key":"value", # format penulisannya
    "cp":"Ucup",
    "tg":"Otong",
    "dg":"dudung",
	'nmbr':100,
	'list':dataList, # bisa untuk seluruh tipe data
}

print(dataDict["tg"]) # penggil menggunakan key-nya 
print(dataDict["nmbr"])
print(dataDict["list"])