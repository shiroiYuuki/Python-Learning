'''Fungsi dengan argument(input)'''

# Template
# def namaFungsi(Argument):
#   Badan fungsi

def helloWorld(nama):
    '''fungsi hello world menerima input dengan variable nama'''
    print(f"Selamat datanng dunia wahai {nama}")
    
helloWorld("Budi")
helloWorld("Cecep")

# Program tambah
def tambah(angka1, angka2):
    '''fungsi tambah'''
    hasil = angka1 + angka2
    print(f"{angka1} + {angka2} = {hasil}")

tambah(1,5)
tambah(100000,1)

def sayHi(listPeserta):
    '''fungsi say hi'''
    dataPeserta = listPeserta.copy() # agar saat di modif data di luar tidak berubah
    for peserta in dataPeserta:
        print(f"Yang terhormat {peserta}")

anggotaBoyband = {"Ucup", "Otong", "Dudung"}

sayHi(anggotaBoyband)