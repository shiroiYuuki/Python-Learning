import datetime

mahasiswa1 = {
    'nama':'Ucup surucup',
    'nim':'190220001',
    'sksLulus':130,
    'beasiswa':False,
    'lahir':datetime.datetime(2001,4,10)
}

mahasiswa2 = {
    'nama':'Otong surutong',
    'nim':'190220002',
    'sksLulus':140,
    'beasiswa':False,
    'lahir':datetime.datetime(2002,10,10)
}

mahasiswa3 = {
    'nama':'Asep si Kasyep',
    'nim':'190220003',
    'sksLulus':100,
    'beasiswa':False,
    'lahir':datetime.datetime(2000,2,29)
}

dataMahasiswa = {
    'MAH001':mahasiswa1,
    'MAH002':mahasiswa2,
    'MAH003':mahasiswa3,
}

print(f"{'KEY':<6} {'Nama':<17} {'SKS':<3} {'Beasiswa':<9} {'Lahir':<10}")
print("-"*50)

for mahasiswa in dataMahasiswa:
    KEY = mahasiswa
    
    NAMA = dataMahasiswa[KEY]['nama']
    NIM = dataMahasiswa[KEY]['nim']
    SKS = dataMahasiswa[KEY]['sksLulus']
    BEASISWA = dataMahasiswa[KEY]['beasiswa']
    LAHIR = dataMahasiswa[KEY]['lahir'].strftime("%x")
    print(f"{KEY:<6} {NAMA:<17} {SKS:<3} {BEASISWA} {LAHIR:<10}")