## Teknik menduplikat list

a = ["Ucup", "Otong", "Dudung"]
print(f"a = {a}")
print(f"a = {a}")

b = a # pass by reference
print(f"b = {b}")
print(f"b = {b}")

# akan merubah member a

# ini akan merubah kedua list
a[1] = "Michael"
b.sort()
print(f"a = {a}")
print(f"b = {b}")

# address dari kedua list a dan b
print(f"address a = {hex(id(a))}")
print(f"address a = {hex(id(a))}")
print(f"address b = {hex(id(b))}") # memliki address yang sama

# menduplikat list dengan copy
print("Membuat list c dengan a.copy()")
c = a.copy() # full duplikat / data baru
print(f"address a = {hex(id(a))}")
print(f"address b = {hex(id(b))}") # memliki address yang sama
print(f"address c = {hex(id(c))}") # memliki address yang berbeda

print(f"a = {a}")
print(f"b = {b}")
print(f"c = {c}")

print("ubah data index 0")
c[0] = "Cecep"
print(f"a = {a}")
print(f"b = {b}")
print(f"c = {c}") # jika "c" di ubah maka yang lain tidak akan terubah

print("ubah data index 1")
a[1] = "Otong"
print(f"a = {a}")
print(f"b = {b}")
print(f"c = {c}")