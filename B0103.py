
# Tugas Praktikum B0103
# Sistem Profil Karakter Game RPG

# 1. Membuat variabel profil karakter
nama_hero = "Arthas"
level = 10
hp = 100.0
is_alive = True
inventory = ["Pedang", "Busur", "Kapak"]
atribut = {
    "kekuatan": 80,
    "kelincahan": 65
}

# 2. Menampilkan seluruh informasi karakter
print("=== PROFIL KARAKTER AWAL ===")
print("Nama Hero:", nama_hero)
print("Level:", level)
print("HP:", hp)
print("Is Alive:", is_alive)
print("Inventory:", inventory)
print("Atribut:", atribut)

# 3. Menampilkan tipe data masing-masing variabel
print("\n=== TIPE DATA ===")
print("Tipe nama_hero:", type(nama_hero))
print("Tipe level:", type(level))
print("Tipe hp:", type(hp))
print("Tipe is_alive:", type(is_alive))
print("Tipe inventory:", type(inventory))
print("Tipe atribut:", type(atribut))

# 4. Melakukan aksi pada karakter
# Menambahkan item baru ke inventory
inventory.append("Ramuan HP")

# Mengubah level menjadi float dan menambahkan 0.5
level = float(level)
level = level + 0.5

# 5. Menampilkan informasi karakter terbaru
print("\n=== PROFIL KARAKTER TERBARU ===")
print("Nama Hero:", nama_hero)
print("Level:", level)
print("HP:", hp)
print("Is Alive:", is_alive)
print("Inventory:", inventory)
print("Atribut:", atribut)

print("\nTipe level terbaru:", type(level))
