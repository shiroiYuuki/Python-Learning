items = "milk\neggs\nbread\nini dari Write data"
file = open(r"D:\Coding\Python\Materi\57. Read external file - open dan with\data.txt", "w") # "w" di gunakan untuk menulis data
# note: data yang ada akan di hapus jika
file.write(items)
file.close()

