# Modul fungsi bantuan umum (opsional)

def format_laporan(statistik, tuntas_count, kkm):
    """Mengformat ringkasan data menjadi string teks laporan."""
    text = "=== LAPORAN HASIL ANALISIS NILAI MATEMATIKA ===\n"
    text += f"Batas KKM           : {kkm}\n"
    text += f"Total Siswa Valid   : {statistik['total_siswa']}\n"
    text += f"Rata-rata Kelas     : {statistik['rata_rata']:.2f}\n"
    text += f"Nilai Tertinggi     : {statistik['maksimum']}\n"
    text += f"Nilai Terendah      : {statistik['minimum']}\n"
    text += f"Jumlah Siswa Tuntas : {tuntas_count}\n"
    text += "===============================================\n"
    return text