<<<<<<< HEAD
# proyek-akhir-dwi-reva-rahmadiniya-2225250070
proyek akhir alpro
=======
# Program Rekap dan Analisis Nilai Matematika Kelas

**Nama:** Dwi Reva Rahmadiniyah  
**NIM:** 2225250070  
**Kelas:** 3E  

## Deskripsi
Program Python untuk mengolah nilai siswa, menghitung statistik, menentukan ketuntasan, dan membuat laporan.

## Fitur
- Membaca data dari file teks.
- Memvalidasi nilai 0-100.
- Menghitung rata-rata, minimum, dan maksimum.
- Menentukan status ketuntasan dengan KKM 75.
- Menyimpan laporan ke file teks.

## Struktur Folder
- `data/`: Data nilai contoh.
- `src/`: Source code program.
- `tests/`: Rancangan pengujian.
- `output/`: Hasil laporan.

## Cara Menjalankan
Pastikan Python sudah terpasang.

Jalankan terminal di folder utama proyek, lalu ketik:

```bash
python src/main.py

## Pengujian
Lihat tests/test_case.md untuk daftar test case.
## Daftar Test Case

| ID | Kategori | Input / Kondisi | Expected Result (Hasil yang Diharapkan) |
| :--- | :--- | :--- | :--- |
| **TC01** | Normal | Nilai siswa: `80, 70, 90` | Rata-rata kelas terhitung dengan benar (`80.0`)[cite: 8]. |
| **TC02** | Batas | Nilai siswa: `0` | Diterima sebagai nilai valid oleh sistem[cite: 8]. |
| **TC03** | Batas | Nilai siswa: `100` | Diterima sebagai nilai valid oleh sistem[cite: 8]. |
| **TC04** | Invalid | Nilai siswa: `105` (di luar rentang 0-100) | Ditolak oleh fungsi validasi dengan pesan error[cite: 8]. |
| **TC05** | Invalid | File sumber tidak ada / salah path (`kosong.txt`) | Program menangani `FileNotFoundError` dengan menampilkan pesan error tanpa *crash*[cite: 8]. |
| **TC06** | Normal | Semua nilai siswa $\ge$ KKM (misal $\ge 75$) | Jumlah siswa tuntas sama dengan total keseluruhan data siswa[cite: 8]. |

## Status
Proyek dalam tahap implementasi dan pengujian.
>>>>>>> f33b331 (docs: menambahkan proposal, struktur folder, dan test case proyek)
