# Looping dictionary

temanTeman = {
    "cup":"Ucup surucup",
    "tong":"Otong surotong",
    "dung":"Dududng surudung",
    "sep":"asep si asep",
    "cuy":"ucuy sicuy"
}

# Looping first try(yang keluar adalah keynya)
for key in temanTeman:
    print(key) # yang keluar adalah keynya
    
# Operator untuk mengambil item/iterables
key = temanTeman.keys() # untuk mengambil key
print(key)

print("\n")


# untuk mengambil value
for key in temanTeman.keys(): # artinya "loop semua KEY"
    print(temanTeman.get(key)) # artinya “ambil VALUE dari KEY tersebut”
    
print("\n")

values = temanTeman.values() # untuk mengambil value
print(values)
print("\n")

for values in temanTeman.values(): # untuk mengambil value pakai looping
    print(values)
print("\n")

items = temanTeman.items() # untuk mengambil items(1 data full)
print(items)
print("\n")

for items in temanTeman.items(): # untuk mengambil items pakai looping
    print(items)
print("\n")

for key,value in temanTeman.items():
    print(f"key = {key}, | value = {value}")