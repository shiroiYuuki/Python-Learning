# Program list buku

listBuku = []
while True:
    print("\nMasukkan data buku")
    judul = input("Judul buku\t: ")
    penulis = input("Nama Penulis\t: ")
    
    bukuBaru = [judul,penulis]
    listBuku.append(bukuBaru)
    print("\n\n","="*10,"Data Buku","="*10)
    for index, buku in enumerate(listBuku):
        print(f"{index+1} | {buku[0]} | {buku[1]}")
    
    print("\n\n","="*20)
    isLanjut = input("Apakah dilanjutkan? (y/n)")
    if isLanjut == "n" or isLanjut == "N":
        break
print("Program Selesai")