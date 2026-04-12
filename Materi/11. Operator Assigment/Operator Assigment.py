# operasi yang dapat di lakukan dengan penyingkatan
# operasi ditambah dengan assignment

a = 5 # adalah assignment
print("Nilai a = ", a)

a += 1 # artinya a = a += 1
print("Nilai += 1, Nilai a Menjadi ", a)

a -= 2 # artinya a = a -= 2
print("Nilai -= 2, Nilai a Menjadi ", a)

a *= 5 # artinya a = a *= 5
print("Nilai *= 5, Nilai a Menjadi ", a)

a /= 2 # artinya a = a /= 2
print("Nilai /= 2, Nilai a Menjadi ", a)

b = 10
print("Nilai b =", b)

b %= 3
print("Nilai %= 3, Nilai b Menjadi ", b)

b = 10
print("Nilai b =", b)

b //= 3
print("Nilai //= 3, Nilai b Menjadi ", b)

a = 5 # adalah assignment
print("Nilai a = ", a)
a **= 3 # ini adalah pangkat
print("Nilai **= 3, Nilai a Menjadi ", a)


# operasi bitwise

# OR
c = True
print("\n nilai c =", c)
c |= False
print("\n nilai c |= false, nilai c menjadi ", c)
c = False
print("\n nilai c =", c)
c |= False
print("\n nilai c |= false, nilai c menjadi ", c)

# AND
c = True
print("\n nilai c =", c)
c &= False
print("\n nilai c &= false, nilai c menjadi ", c)
c = True
print("\n nilai c =", c)
c &= True
print("\n nilai c &= True, nilai c menjadi ", c)

# XOR
c = True
print("\n nilai c =", c)
c ^= False
print("\n nilai c ^= false, nilai c menjadi ", c)
c = True
print("\n nilai c =", c)
c ^= True
print("\n nilai c ^= True, nilai c menjadi ", c)

# geser geser
d = 0b0100
print("\n Nilai d =", format(d,'04b'))
d >>= 2
print("\n Nilai d >>=, nilai d menjadi ", format(d,'04b'))
d <<= 1
print("\n Nilai d <<=, nilai d menjadi ", format(d,'04b'))
