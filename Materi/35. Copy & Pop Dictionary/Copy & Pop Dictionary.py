# Copy dictionary

temanTeman = {
    "cup":"Ucup surucup",
    "tong":"Otong surotong",
    "dung":"Dududng surudung",
    "sep":"asep si asep",
    "cuy":"ucuy sicuy"
}

friends = temanTeman.copy() # untuk menjadikan 2 hal yang berbeda

print(f"teman teman: {temanTeman}\n")
print(f"friends: {friends}\n")

temanTeman["cup"] = "ucup si keren"
print(f"teman teman: {temanTeman}\n")
print(f"friends: {friends}\n")

# Pop dictionary
dataAsep = friends.pop("sep") # datanya di transfer dari friends ke asep
print(f"data asep {dataAsep}")
print(f"friends: {friends}\n")

# Popitem Dictionary
dataTerakhir = friends.popitem() # yang di ambil adalah items(sepasang)
print(f"data Terakhir {dataTerakhir}")
print(f"friends: {friends}\n") # datanya hilang tapi yang terakhir