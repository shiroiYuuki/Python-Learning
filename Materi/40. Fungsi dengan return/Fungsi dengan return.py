'''fungsi dengan kembalian(return)'''

# Template fungsi dengan kembalian
# def namaFungsi(argument):
#   badan fungsi
#   return output

# Fungsi kuadrat
def kuadrat(inputAngka):
    '''fungsi kuadrat'''
    output = inputAngka**2 # argument di pangkat 2
    return output

y = kuadrat(5)
print(y)

print(kuadrat(9)) # bisa untuk seperti ini

z = 10 + kuadrat(7)
print(z)

# fungsi tambah

def fungsiTambah(angka1,angka2):
    '''fungsi return dengan multiInput'''
    return angka1+angka2

a = fungsiTambah(10,9)
print(a)

# fungsi dengan return banyak
def operasiMatematika(angka1, angka2):
    tambah = angka1 + angka2
    kurang = angka1 - angka2
    kali = angka1 * angka2
    bagi = angka1 / angka2
    return tambah,kurang,kali,bagi

k,l,m,n = operasiMatematika(9,5)
print(f"Hasil tambah = {k}")
print(f"Hasil kurang = {l}")
print(f"Hasil kali = {m}")
print(f"Hasil bagi = {n}")