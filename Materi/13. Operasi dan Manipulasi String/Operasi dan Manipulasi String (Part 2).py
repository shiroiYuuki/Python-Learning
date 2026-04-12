# Operator dalam bentuk method

## merubah case pada string

salam = "bro!"
print("normal " + salam)
salam = salam.upper()
print("upper " + salam)

# merubah semua ke lower case
alay = "aKu KeCe AbieeZZZ"
print("normal " + alay)
alay = alay.lower()
print("lower " + alay)

## method is, untuk pengecekan

# contoh isupper()
salam = "SIST"
apakahUpper = salam.isupper()
print(salam + " is upper " + str(apakahUpper))
salam = salam.lower()
apakahUpper = salam.isupper()
print(salam + " is upper? " + str(apakahUpper))

# islower() <- untuk pengecekan apakah lower case semua
# isalpha() <- untuk mengecek apakah huruf semua
# isalnum() <- apakah huruf dan angka
# isdecimal() <- apakah numeric
# isspace() <- apakah isinya spasi, tab dan enter (newline \n)
# istitle() <- huruf pertama setiap kata upper case

judul = "It Is Okay To Not Be Orkay"
cek_judul = judul.istitle()
print(judul + " is title? " + str(cek_judul))

# startwith() dan endwith() <-- keren

cek_start = "Sangjangnim Oppa".startswith("Sangjangnim") # mengecek apakah awalnya ada Sangjangnim
print("start " + str(cek_start))
cek_end = "Sangjangnim Oppak".endswith("Oppak")
print("end " + str(cek_end))

# join() dan split() <-- buat orang males

pisah = ['aku','sayang','kamu']
gabungan = ' ehm '.join(pisah) # akan ada ehm di antara kalimat
print(pisah)
print(gabungan)

gabungan = "naik vespa keliling kota"
pisah = gabungan.split() # akan memisahkan kalimat di atas dan menjadi list
print(gabungan)
print(pisah)

gabungan = "naikehmvespaehmkelilingehmkota"
pisah = gabungan.split("ehm") # menghilangkan kata "ehm"
print(gabungan)
print(pisah)

# alokasi karakter
print("'kiri      '")

kanan = "kanan".rjust(20) # rata kanan dengan 20 karakter
print("'" + kanan + "'")

kiri = "kiri".ljust(20) # rata kiri dengan 20 karakter
print("'" + kiri + "'")

tengah ="tengah".center(20) # rata tengah dengan 20 karakter
print("'" + tengah + "'")

tengah ="tengah".center(20,'-') # rata tengah dengan 20 karakter
print("'" + tengah + "'")

# kebalikan dari alokasi karakter
kanan = kanan.strip()
print("'" + kanan + "'")
tengah = tengah.strip('-')
print("'" + tengah + "'")