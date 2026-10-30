# Modul untuk fungsi statistik matematika dan KKM

def hitung_statistik(data_siswa):
    """Menghitung rata-rata, min, dan max nilai."""
    if not data_siswa:
        return None
    
    nilai_list = list(data_siswa.values())
    rata_rata = sum(nilai_list) / len(nilai_list)
    nilai_min = min(nilai_list)
    nilai_max = max(nilai_list)
    
    return {
        "rata_rata": rata_rata,
        "minimum": nilai_min,
        "maksimum": nilai_max,
        "total_siswa": len(nilai_list)
    }

def analisis_ketuntasan(data_siswa, kkm=75):
    """Menentukan status ketuntasan siswa berdasarkan nilai KKM."""
    hasil_ketuntasan = {}
    tuntas_count = 0
    
    for nama, nilai in data_siswa.items():
        if nilai >= kkm:
            status = "Tuntas"
            tuntas_count += 1
        else:
            status = "Belum Tuntas"
        hasil_ketuntasan[nama] = {"nilai": nilai, "status": status}
        
    return hasil_ketuntasan, tuntas_count