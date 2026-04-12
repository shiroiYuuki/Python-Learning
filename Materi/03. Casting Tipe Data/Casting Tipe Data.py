#  casting adalah merubah satu tipe data ke tipe data yang lain
# tipe data = int, float, str, bool

## INTEGER
print("=====INTEGER=====")
dataInt = 8;
print("data = ", dataInt, ", type =", type(dataInt))

dataFloat = float(dataInt)
print("Data = ", dataFloat, ", type = ", type(dataInt))
dataStr = str(dataInt)
print("Data = ", dataStr, ", type = ", type(dataInt))
dataBool = bool(dataInt) # akan false jika nilai Int = 0
print("Data = ", dataBool, ", type = ", type(dataInt))

## Float
print("=====Float=====")
dataFloat = 9.9;
print("data = ", dataFloat, ", type =", type(dataFloat))

dataInt = int(dataFloat)
print("Data = ", dataInt, ", type = ", type(dataInt)) # akan di bulatkan ke bawah
dataStr = str(dataFloat)
print("Data = ", dataStr, ", type = ", type(dataStr))
dataFloat = 9.9;
dataBool = bool(dataFloat) # akan True jika nilai float > 0
print("Data = ", dataBool, ", type = ", type(dataBool))
dataFloat = 0;
dataBool = bool(dataFloat) # akan false jika nilai float = 0
print("Data = ", dataBool, ", type = ", type(dataBool))

## Boolean
print("=====Boolean=====")
dataBool = -9;
print("data = ", dataBool, ", type =", type(dataBool))

dataInt = int(dataBool)
print("Data = ", dataInt, ", type = ", type(dataInt)) # akan di bulatkan ke bawah
dataStr = str(dataBool)
print("Data = ", dataStr, ", type = ", type(dataStr))
dataFloat = bool(dataFloat) # akan false jika nilai float = 0 dan akan true jika </> 0
print("Data = ", dataFloat, ", type = ", type(dataFloat))

