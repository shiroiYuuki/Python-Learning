import os

print("=" * 5, " Membaca file txt ", "=" * 5)

# 1. Gunakan satu path (pakai raw string biar aman di Windows)
path = r"D:\Coding\Python\Materi\57. Read external file - open dan with\data.txt"

# 2. Validasi apakah file ada
if not os.path.exists(path):
    print("Error: file tidak ditemukan")
    print("Cek kembali path kamu!")
    exit(1)

# 3. Gunakan with (auto close)
with open(path, mode="r") as file:
    print(f"status read : {file.readable()}")
    print(f"status write : {file.writable()}")

    print("\nIsi file:")
    print(file.read())

    print(f"\napakah file sudah diclose (di dalam with): {file.closed}")

# 4. Setelah keluar dari with
print(f"apakah file sudah diclose (di luar with): {file.closed}")
