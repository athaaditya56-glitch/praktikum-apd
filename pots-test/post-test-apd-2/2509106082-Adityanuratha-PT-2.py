# Input data mahasiswa
nama = input("Masukkan Nama Lengkap: ")
nim = input("Masukkan NIM: ")
harga = float(input("Masukkan harga menu makanan (Rp): "))

# Data menu dan pajak (pakai dictionary agar tidak pakai if/else)
menu_pajak = {
    "Pecel Lele": 5,
    "Mie Ayam": 8,
    "Nasi Padang": 10
}

print(f"\n{nama} dengan NIM {nim} ingin membeli makanan seharga Rp{harga:.0f}")

# Perulangan untuk setiap menu
for menu, persen in menu_pajak.items():
    pajak = harga * (persen / 100)
    total = harga + pajak
    print(f"Jika dia membeli {menu}, maka ia harus membayar Rp{total:.0f} setelah mendapat pajak {persen}%.")