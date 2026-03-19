# format string

# contoh generic
# string
nama = "ucup"
formatStr = f"hello {nama}"
print(formatStr)

# boolean
boolean = True
formatStr = f"boolean = {boolean}"
print(formatStr)

# angka
angka = 2005.5
formatStr = f"angka = {angka}"
print(formatStr)

# bilangan bulat
angka = 15
formatStr = f"bilangan bulat = {angka:d}" # untuk memastikan angka yang ada di variable adalah bil. bulat
print(formatStr)

# bilangan dengan ordo ribuan
angka = 2000000
formatStr = f"ribuan = {angka:,}" # meletakkan koma di setiap 3 angka
print(formatStr)

# bilangan desimal
angka = 2005.54321
formatStr = f"desimal = {angka:.3f}" # mengambil 3 angka di belakang koma dan memberitau ini float
print(formatStr)

# menampilkan leading zero
angka = 2005.54321
formatStr = f"leading zero = {angka:010.3f}" # tampilkan angka float dengan 3 desimal, panjang 10 karakter, dan isi kosongnya dengan nol di depan.
print(formatStr)

# menampilkan tanda (+) dan (-)
angkaMinus = -10
angkaPlus = +15.34532
formatMinus = f"Minus = {angkaMinus:+d}"
formatPlus = f"Plus = {angkaPlus:+.2f}"
print(formatMinus)
print(formatPlus)

# menformat persen
persentase = 0.045
formatPersen = f"Persen = {persentase:.2%}"
print(formatPersen)

# melakukan operasi aritmatika di dalam placeholder
harga = 1000
jumlah = 5

formatString = f"Harga total = Rp. {harga*jumlah:,}"
print(formatString)

# format angka lain (binary, octal, hexadecimal)
angka = 255
formatBinary = f"Binary = {bin(angka)}"
formatOctal = f"Octal = {oct(angka)}"
formatHex = f"Hex = {hex(angka)}"

print(formatBinary)
print(formatOctal)
print(formatHex)