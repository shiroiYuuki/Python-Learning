import datetime

dataWaktu = datetime.datetime.now() # untuk mengambil waktu sekarang
print(f"datetime now : {dataWaktu}")
print(f"tahun : {dataWaktu.year}") # untuk menunjukkan tahun
print(f"hari : {dataWaktu.strftime('%A')}") # untuk menunjukkan hari

from collections import Counter

data = ["a", "b", "c", "d", "a", "d", "a"]
dataCount = Counter(data)

print(f"data count = {dataCount}")
print(f"jumlah data a = {dataCount['a']}")
print(f"jumlah data d = {dataCount['d']}")

import io

file = io.open(r"D:/Coding/Python/Materi/52. Menggunakan Standard Library/fileText.txt","r") # untuk membuka file dan membacanya
print(file.read())

