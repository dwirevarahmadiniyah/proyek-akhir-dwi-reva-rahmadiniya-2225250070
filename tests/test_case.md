# Rencana Pengujian (Test Case) Proyek Akhir

Dokumen ini berisi daftar skenario pengujian untuk memastikan program berjalan dengan valid, dapat menangani batasan angka, serta mencegah error (*crash*) akibat kesalahan input atau file.

## Daftar Test Case

| ID | Kategori | Input / Kondisi | Expected Result (Hasil yang Diharapkan) |
| :--- | :--- | :--- | :--- |
| **TC01** | Normal | Nilai siswa: `80, 70, 90` | Rata-rata kelas terhitung dengan benar (`80.0`)[cite: 8]. |
| **TC02** | Batas | Nilai siswa: `0` | Diterima sebagai nilai valid oleh sistem[cite: 8]. |
| **TC03** | Batas | Nilai siswa: `100` | Diterima sebagai nilai valid oleh sistem[cite: 8]. |
| **TC04** | Invalid | Nilai siswa: `105` (di luar rentang 0-100) | Ditolak oleh fungsi validasi dengan pesan error[cite: 8]. |
| **TC05** | Invalid | File sumber tidak ada / salah path (`kosong.txt`) | Program menangani `FileNotFoundError` dengan menampilkan pesan error tanpa *crash*[cite: 8]. |
| **TC06** | Normal | Semua nilai siswa $\ge$ KKM (misal $\ge 75$) | Jumlah siswa tuntas sama dengan total keseluruhan data siswa[cite: 8]. |