# File utama pengeksekusi program

from data_io import baca_data, simpan_laporan
from analisis import hitung_statistik, analisis_ketuntasan
from utilitas import format_laporan

def main():
    print("=== PROGRAM REKAP NILAI MATEMATIKA ===")
    file_input = "data/nilai_contoh.txt"
    file_output = "output/laporan.txt"
    kkm_target = 75

    # 1. Baca Data
    data = baca_data(file_input)
    if not data:
        print("[SISTEM] Program dihentikan karena data kosong atau error.")
        return

    # 2. Hitung Statistik & Ketuntasan
    stats = hitung_statistik(data)
    hasil_kkm, tuntas_count = analisis_ketuntasan(data, kkm=kkm_target)

    # 3. Format & Tampilkan Hasil
    laporan_text = format_laporan(stats, tuntas_count, kkm_target)
    print("\n" + laporan_text)

    # 4. Simpan Laporan
    simpan_laporan(file_output, laporan_text)

if __name__ == "__main__":
    main()