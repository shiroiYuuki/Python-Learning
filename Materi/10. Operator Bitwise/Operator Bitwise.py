# Operator Bitwise, Bitwise itu adalah Operasi pada masing masing bit

a = 9
b = 5

# Operator Bitwise OR (|)
c = a | b
print("\n====OR====")
print("NIlai ", a, " , Binary :", format(a, '08b'))
print("NIlai ", b, " , Binary :", format(b, '08b'))
print('------------(|)')
print("NIlai ", c, " , Binary :", format(c, '08b'))


# Operator Bitwise (&)
c = a & b
print("\n====Bitwise====")
print("NIlai ", a, " , Binary :", format(a, '08b'))
print("NIlai ", b, " , Binary :", format(b, '08b'))
print('------------(&)')
print("NIlai ", c, " , Binary :", format(c, '08b'))

# Operator XOR (^)
c = a ^ b
print("\n====XOR====")
print("NIlai ", a, " , Binary :", format(a, '08b'))
print("NIlai ", b, " , Binary :", format(b, '08b'))
print('------------(^)')
print("NIlai ", c, " , Binary :", format(c, '08b'))

# Operator NOT (~)
c = ~a
print("\n====NOT====")
print("NIlai ", a, " , Binary :", format(a, '08b'))
print('------------(~)')
print("NIlai ", c, " , Binary :", format(c, '08b'))
print('------------(^)')
d = 0b0000001001
e = 0b1111111111 
print("Nilai :", e^d, " , Binary :", format(e^d, '08b'))

# Shifting

# Shift Right (>>)
c = a >> 2
print("\n====Shift Right====")
print("NIlai ", a, " , Binary :", format(a, '08b'))
print('------------(>>)')
print("NIlai ", c, " , Binary :", format(c, '08b'))

# Shift Left (<<)
c = a << 2
print("\n====Shift Left====")
print("NIlai ", a, " , Binary :", format(a, '08b'))
print('------------(>>)')
print("NIlai ", c, " , Binary :", format(c, '08b'))