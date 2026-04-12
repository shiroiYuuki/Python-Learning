# episode Latihan Logika dan komperasi
# Membuat gabungan area rentang dari angka

# +++++++3---------10+++++++
inputUser = float(input("Masukkan angka yang bernilai kurang dari 3 \n atau \n lebih dari 10 \n: "))
# data hasil input user pasti string, maka harus di casting dulu ke int/float

# ++++++3-----------
# memeriksa apakah angka kurang dari 3
isKurangDari = (inputUser < 3)
print("Kurang dari 3: ", isKurangDari)


# -----------10+++++++
#memeriksa apakah angka lebih dari 10
isLebihDari = (inputUser > 10)
print("Lebih dari 10: ", isLebihDari)

# +++3-----------------10++++
isCorrect = isKurangDari or isLebihDari
print("yang anda masukkan itu: ", isCorrect)

#----3+++++++++++++++++10-----
# kasus irisan
print("\n",10*"=","\n")
inputUser = float(input("Masukkan angka yang bernilai lebih dari 3 \n dan \n kurang dari 10 \n: "))


# --------3+++++++
# lebih dari 3
isLebihDari = inputUser > 3
print("Lebih dari 3: ", isLebihDari)

# ++++++++10------
#kurang dari 10
isKurangDari = inputUser < 10
print("Kurang dari 10", isKurangDari)

#----3+++++++++++++++++10-----
isCorrect = isKurangDari and isLebihDari
print("yang anda masukkan itu: ", isCorrect)
