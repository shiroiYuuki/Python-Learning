import sains.matematika # cara memanggil modul pertama
from sains import fisika # cara memanggil modul kedua
from sains.fisika import gaya as force # hanya mengambil function gaya, 
# dan mengubah namanya menjadi force(jadi memiliki 2 nama)

hasilTambah = sains.matematika.tambah(1,2,3,4,5)
print(f"hasil tambahan dari package di atas adalah = {hasilTambah}")

gaya = fisika.gaya(90,10)
print(f"gaya adalah = {gaya}")

gaya = force(90,10)
print(f"gaya adalah = {gaya}")
