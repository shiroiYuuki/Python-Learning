'''Default argumen'''

# def fungsi(argumen):
# def fungsi(argumen = nilai defaultnya)

# contoh 1
def sayHello(nama = "Ganteng"):
    '''fungsi dengan default argumen'''
    print(f"hello {nama}")
    
sayHello("Budi")
sayHello()

# contoh 2
def sapaDia(nama, pesan = "Apa kabar"):
    '''fungsi dengan satu input biasa, dan satu default argumen'''
    print(f"Hai {nama}, {pesan}")

sapaDia("Dudung", "Haiiiiii")
sapaDia("Otong")

# contoh 3
def hitungPangkat(angka,pangkat):
    hasil = angka**pangkat
    return hasil

print(hitungPangkat(2,4))

hasil = hitungPangkat(pangkat=3, angka = 5) # defaultnya bisa disini
print(hasil)

# contoh 4
def fungsi(input1=1,input2=2,input3=3,input4=4):
    hasil = input1 + input2 + input3 + input4
    return hasil

print(fungsi())
print(fungsi(input3=10)) # bisa modif cuman aja