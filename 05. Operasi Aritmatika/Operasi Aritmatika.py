# operasi aritmatika

a = 10
b = 3

# operasi tambah +
hasil = a + b
print(a, " + ", b, " = ", hasil)


# operasi pengurangan - 
hasil = a - b
print(a, " - ", b, " = ", hasil)


# operasi perkalian * 
hasil = a * b
print(a, " * ", b, " = ", hasil)

# operasi pembagian /, hasilnya akan otomatis menampilkan float
hasil = a / b
print(a, " / ", b, " = ", hasil)

# operasi eksponen (pangkat) **
hasil = a ** b
print(a, " ** ", b, " = ", hasil)

# operasi modulus %
hasil = a % b
print(a, " % ", b, " = ", hasil)

# operasi floor division, akan di bulatkan ke bawah
hasil = a // b
print(a, " // ", b, " = ", hasil)

# prioritas operasi, operational precendence 
x = 3
y = 2
z = 4

hasil = x ** y * z + x / y - y % z // x
print(x,"**",y,"*",z,"+",x,"/",y,"-",y,"%",z,"//",x, "=", hasil)
# 1. () 2. exponen 3. perkalian 4. pertambahan dan pengurangan

hasil = x + y + z
print(x, ' + ', y, ' * ', z, ' = ', hasil)