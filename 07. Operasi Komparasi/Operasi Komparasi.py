# operasi komperasi

# setiap hasil dari hasil komparasi adalah boolean

# >,<,>=, <=, ==, !=, is, is not

a = 4
b = 2

# lebih besar dari >
print('===ini lebih besar dari (>)===')
hasil = a > 3
print(a, '>', 3, '=', hasil)
hasil = b > 3
print(b, '>', 3, '=', hasil)
hasil = b > 4
print(b, '>', 4, '=', hasil)

# lebih kecil dari <
print('===ini lebih kecil dari (<)===')
hasil = a < 3
print(a, '<', 3, '=', hasil)
hasil = b < 3
print(b, '<', 3, '=', hasil)
hasil = b < 4
print(b, '<', 4, '=', hasil)


# lebih dari sama dengan dari >=
print('===ini lebih lebih dari sama dengan (>=)===')
hasil = a >= 3 
print(a, '>=', 3 , '=', hasil)
hasil = b >= 3
print(b, '>=', 3, '=', hasil)
hasil = b >= 2
print(b, '>=', 2, '=', hasil)

# kurang dari sama dengan dari >=
print('===ini kurang dari sama dengan (>=)===')
hasil = a <= 3 
print(a, '<=', 3 , '=', hasil)
hasil = b <= 3
print(b, '<=', 3, '=', hasil)
hasil = b <= 2
print(b, '<=', 2, '=', hasil)

# sama dengan (==)
print('===ini sama dengan (==)===')
hasil = a == 4
print(a, '==', 4, '=', hasil)
hasil = b == 4
print(b, '==', 4, '=', hasil)
# = ini adalah assigment
# == kalo ini namanya membandingkan

# tidak sama dengan (!=)
print('===ini tidak sama dengan (!=)===')
hasil = a != 4
print(a, '!=', 4, '=', hasil)
hasil = b != 4
print(b, '!=', 4, '=', hasil)

print('===object identity (is)===')
# 'is' sebagai komparasi object identity
x = 5 # ini adalah assigment membuat object
y = 5
print("nilai x adalah ", x, "id = ", hex(id(x)))
print("nilai y adalah ", y, "id = ", hex(id(y))) # kalo ada object yang nilainya sama maka akan di letakkan di memori yang sama
hasil = x is y # jangan membandingkan object dengan literal kalo menggunakan 'is' kalo literal mending pakai '=='
print('x is y = ', hasil)


print('===object identity (is not)===')
# 'is' sebagai komparasi object identity
x = 5 # ini adalah assigment membuat object
y = 5
print("nilai x adalah ", x, "id = ", hex(id(x)))
print("nilai y adalah ", y, "id = ", hex(id(y))) # kalo ada object yang nilainya sama maka akan di letakkan di memori yang sama
hasil = x is not y # akan false karena sama
print('x is y = ', hasil)