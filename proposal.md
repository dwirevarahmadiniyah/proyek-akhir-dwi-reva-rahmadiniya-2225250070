# Proposal Proyek Akhir: Program Rekap dan Analisis Nilai Matematika

## 1. Judul Proyek
Program Rekap dan Analisis Nilai Ujian Matematika Berbasis Konsol

## 2. Masalah dan Latar Belakang
Guru matematika sering kali membutuhkan waktu lama untuk merekap nilai ujian siswa secara manual, menghitung rata-rata kelas, menentukan nilai minimum/maksimum, serta mengecek status kelulusan berdasarkan Kriteria Ketuntasan Minimal (KKM). Proyek ini bertujuan menyediakan program berbasis terminal (Python) untuk membaca data nilai, melakukan kalkulasi statistik otomatis, dan menyimpan hasilnya ke file laporan.

## 3. Pengguna dan Tujuan
- **Pengguna Utama:** Guru Matematika
- **User Story:** "Sebagai guru matematika, saya ingin memasukkan atau membaca data nilai siswa dari file, agar saya dapat memperoleh statistik dan status ketuntasan siswa secara otomatis."
- **Tujuan:** Otomasi rekapitulasi nilai dan efisiensi pembuatan laporan hasil belajar.

## 4. Fitur Program
1. Membaca data nilai dari file teks (`data/nilai_contoh.txt`).
2. Memvalidasi nilai input (rentang 0-100).
3. Menghitung rata-rata, nilai minimum, dan nilai maksimum kelas.
4. Menentukan status ketuntasan siswa berdasarkan KKM.
5. Menyimpan laporan ringkas ke file eksternal (`output/laporan.txt`).

## 5. Input - Proses - Output (IPO)
- **Input:** File teks berisi nama dan nilai siswa (`nilai_contoh.txt`).
- **Proses:** Validasi format -> Perhitungan statistik -> Penentuan status KKM.
- **Output:** Tampilan statistik di terminal & file laporan hasil rekap (`laporan.txt`).

## 6. Algoritma (Pseudocode)
```text
MULAI
  Baca data dari file path
  JIKA file tidak ditemukan:
    Tampilkan pesan error
    SELESAI
  
  UNTUK setiap baris data:
    Validasi rentang nilai 0 - 100
    Simpan data valid ke dictionary/list
  
  Hitung rata-rata, nilai minimum, nilai maksimum
  Tentukan status ketuntasan berdasarkan KKM
  Tampilkan ringkasan ke konsol
  Simpan laporan ke file keluaran
SELESAI