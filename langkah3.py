
# ==========================================
# PROJECT ALGORITMA DAN PEMROGRAMAN
# LANGKAH 3: TIPE DATA KOLEKSI (NON-PRIMITIVE)
# ==========================================

# 1. LIST (Berurutan, bisa diubah / mutable)
hobi = ["Membaca", "Koding", "Berenang"]

print("=== 1. LIST ===")
print("List Hobi:", hobi)
print("Tipe:", type(hobi))

# 2. TUPLE (Berurutan, tidak bisa diubah / immutable)
koordinat = (-6.1751, 106.8650)

print("\n=== 2. TUPLE ===")
print("Tuple Koordinat:", koordinat)
print("Tipe:", type(koordinat))

# 3. DICTIONARY (Pasangan Key : Value)
mahasiswa = {
    "nama": "Siti",
    "nim": "123456",
    "ipk": 3.85
}

print("\n=== 3. DICTIONARY ===")
print("Dict Mahasiswa:", mahasiswa)
print("Nama Mahasiswa:", mahasiswa["nama"])
print("Tipe:", type(mahasiswa))

# 4. SET (Nilai unik, tidak berurutan, tanpa duplikat)
angka_unik = {1, 2, 2, 3, 4, 4, 5}

print("\n=== 4. SET ===")
print("Set Angka Unik (otomatis menghapus duplikat):", angka_unik)
print("Tipe:", type(angka_unik))
