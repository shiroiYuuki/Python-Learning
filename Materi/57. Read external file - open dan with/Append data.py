items = "Membahkan nasi padang"
file = open(r"D:\Coding\Python\Materi\57. Read external file - open dan with\data.txt", "a") # "a" di gunakan untuk menambah data
# note: tanpa menghapus data yang sudah ada
file.write(items)
file.close()

