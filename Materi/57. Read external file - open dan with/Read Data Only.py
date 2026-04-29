file = open(r"D:\Coding\Python\Materi\57. Read external file - open dan with\data.txt", "r")
contents = file.read()
file.close() 

items = contents.split("\n") # untuk memotong bagian spasi
items.sort()

for item in items:
    print("- " + item)