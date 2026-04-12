'''Type hints untuk fungsi'''

# bentuk standar fungsi yang udah di pelajari

'''
studi kasus
def fungsi(parameter):
    hasil = parameter**2
    print(hasil)

fungsi(1)
fungsi("Ucup")
fungsi(True)
'''

# penggunaan type hints

import string

def sepuluhPangkat(argument:int):
    '''fungsi dengan hints'''
    output = 10**argument
    return output

hasil = sepuluhPangkat(4)
print(hasil)

def display(argument:string):
    print(argument)

display("Ucup")


# type hint di Python digunakan untuk memberi 
# tahu tipe data agar kode lebih mudah dipahami 
# dan dicek kesalahannya sebelum dijalankan.