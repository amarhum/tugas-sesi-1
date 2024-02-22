print("="*30)
print("Menghitung Umur")

from datetime import datetime

def hitung_umur(tahun_lahir):
    tahun_sekarang = datetime.now().year
    umur = tahun_sekarang - tahun_lahir
    return umur

tahun_lahir = int(input("Masukkan tahun lahir: "))
umur = hitung_umur(tahun_lahir)
print("Umur Anda adalah:", umur, "tahun")

print("="*30)
print("menghitung Kembalian")

def hitung_kembalian(total_belanja, uang_dibayarkan):
    kembalian = uang_dibayarkan - total_belanja
    return kembalian

total_belanja = float(input("Masukkan total belanja: "))
uang_dibayarkan = float(input("Masukkan uang yang dibayarkan: "))

if uang_dibayarkan < total_belanja:
    print("Maaf, uang yang dibayarkan kurang dari total belanja.")
else:
    kembalian = hitung_kembalian(total_belanja, uang_dibayarkan)
    print("Uang kembalian:", kembalian)

def hitung_total_belanja(harga_barang, jumlah_barang):
    return harga_barang * jumlah_barang

def hitung_diskon(total_belanja, diskon=0):
    if total_belanja > 60000:
        return diskon
    else:
        return 0
    
print("="*30)
print("menghitung diskon")
harga_barang = float(input("Masukkan harga barang per item: "))
jumlah_barang = int(input("Masukkan jumlah barang yang dibeli: "))

total_belanja = hitung_total_belanja(harga_barang, jumlah_barang)
diskon = hitung_diskon(total_belanja, diskon=10000)
total_harus_dibayar = total_belanja - diskon

print("Total belanja: Rp.", total_belanja)
print("Diskon: Rp.", diskon)
print("Total yang harus dibayar: Rp.", total_harus_dibayar)

print("="*30)
print("menghitung gaji")
def hitung_gaji(gaji_pokok, hari_transport, hari_makan, jam_lembur):
    total_transport = hari_transport * 100000
    total_makan = hari_makan * 50000

    upah_lembur = 0
    if jam_lembur <= 2:
        upah_lembur = jam_lembur * 100000
    else:
        upah_lembur = 200000 + (jam_lembur - 2) * 150000

    honor = gaji_pokok + total_transport + total_makan + upah_lembur
    return honor

gaji_pokok = float(input("Masukkan gaji pokok: "))
hari_transport = int(input("Masukkan jumlah hari transport: "))
hari_makan = int(input("Masukkan jumlah hari makan: "))
jam_lembur = int(input("Masukkan jumlah jam lembur: "))

total_gaji = hitung_gaji(gaji_pokok, hari_transport, hari_makan, jam_lembur)
print("Total gaji adalah:", total_gaji)
