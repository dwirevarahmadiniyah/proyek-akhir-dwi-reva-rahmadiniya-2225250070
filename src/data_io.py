# Modul untuk penanganan input/output file dan validasi data

def validasi_nilai(nilai_str):
    """Memvalidasi apakah input angka dan berada di rentang 0-100."""
    try:
        nilai = float(nilai_str)
        if 0 <= nilai <= 100:
            return True, nilai
        return False, None
    except ValueError:
        return False, None

def baca_data(path_file):
    """Membaca file data nilai dan mengembalikan dictionary data valid."""
    data_siswa = {}
    try:
        with open(path_file, 'r') as file:
            for line in file:
                line = line.strip()
                if not line:
                    continue
                parts = line.split(',')
                if len(parts) == 2:
                    nama, nilai_str = parts[0].strip(), parts[1].strip()
                    is_valid, nilai = validasi_nilai(nilai_str)
                    if is_valid:
                        data_siswa[nama] = nilai
        return data_siswa
    except FileNotFoundError:
        print(f"[ERROR] File '{path_file}' tidak ditemukan.")
        return None

def simpan_laporan(path_output, ringkasan_text):
    """Menulis hasil laporan ke file output."""
    try:
        with open(path_output, 'w') as file:
            file.write(ringkasan_text)
        print(f"[INFO] Laporan berhasil disimpan ke {path_output}")
    except Exception as e:
        print(f"[ERROR] Gagal menyimpan file: {e}")