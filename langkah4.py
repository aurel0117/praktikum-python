
# ==========================================
# PROJECT ALGORITMA DAN PEMROGRAMAN
# LANGKAH 4: PEMBARUAN VARIABEL (STATE UPDATE)
# ==========================================

# Data awal mahasiswa
daftar_matkul = [
    "Algoritma dan Pemrograman",
    "Matematika Diskrit",
    "Basis Data"
]

# Nilai angka mahasiswa
nilai_awal = [85, 90, 87]

# Transkrip nilai mutu
transkrip_nilai = {
    "Algoritma dan Pemrograman": 3.7,
    "Matematika Diskrit": 4.0,
    "Basis Data": 3.7
}

# Menghitung total nilai awal
total_nilai = sum(nilai_awal)

# Menghitung jumlah mata kuliah awal
jumlah_matkul = len(daftar_matkul)

# Menghitung rata-rata awal
rata_rata = total_nilai / jumlah_matkul

# 6. UPDATE VARIABEL DINAMIS
# Mahasiswa mengambil 1 mata kuliah susulan

matkul_baru = "Jaringan Komputer"
nilai_matkul_baru_str = "88.0"
mutu_matkul_baru = 3.5  # Nilai AB

# A. Tambahkan ke List
daftar_matkul.append(matkul_baru)

# B. Tambahkan ke Dictionary
transkrip_nilai[matkul_baru] = mutu_matkul_baru

# C. Rekalkulasi Variabel Total & Rata-rata
nilai_jk = float(nilai_matkul_baru_str)

total_nilai = total_nilai + nilai_jk
jumlah_matkul = len(daftar_matkul)
rata_rata_terbaru = total_nilai / jumlah_matkul

# D. Hitung IPK dari Dictionary Mutu
total_bobot_mutu = sum(transkrip_nilai.values())
ipk_sementara = total_bobot_mutu / jumlah_matkul

# Menampilkan hasil
print("\n=== HASIL REKALKULASI SETELAH PENAMBAHAN MATKUL ===")
print("Daftar Matkul Terbaru:", daftar_matkul)
print("Jumlah Matkul Total:", jumlah_matkul)
print("Total Nilai:", total_nilai)
print("Rata-Rata Angka Baru:", round(rata_rata_terbaru, 2))
print("IPK Sementara (Skala 4):", round(ipk_sementara, 2))
