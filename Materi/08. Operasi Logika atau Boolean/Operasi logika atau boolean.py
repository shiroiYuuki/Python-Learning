# operasi logika atau boolean

# not, or, and , xor

# NOT
print("===NOT===")
a = False
c = not a
print("data a = ", a)
print("----------Not ")
print("data c = ", c)

# OR
print("===OR===") # jika salah satunya true maka akan true
a = True
b = False
c = a or b
print(a, 'or', b, '=', c)

a = True
b = True
c = a or b
print(a, 'or', b, '=', c)

a = False
b = False
c = a or b
print(a, 'or', b, '=', c)

a = False
b = True
c = a or b
print(a, 'or', b, '=', c)

# AND
print("===AND===") # akan true jika kedua keduanya true
a = True
b = False
c = a and b
print(a, 'and', b, '=', c)

a = True
b = True
c = a and b
print(a, 'and', b, '=', c)

a = False
b = False
c = a and b
print(a, 'and', b, '=', c)

a = False
b = True
c = a and b
print(a, 'and', b, '=', c)

# XOR ini adalah operator bitwise, bukan operasi logika
print("===XOR===") # akan true jika truenya hanya satu
a = True
b = False
c = a ^ b
print(a, 'XOR', b, '=', c)

a = True
b = True
c = a ^ b
print(a, 'XOR', b, '=', c)

a = False
b = False
c = a ^ b
print(a, 'XOR', b, '=', c)

a = False
b = True
c = a ^ b
print(a, 'XOR', b, '=', c)
