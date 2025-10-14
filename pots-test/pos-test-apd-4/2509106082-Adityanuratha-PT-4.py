usernameAkun = "Aditya nur atha"   
passwordAkun = "2509106082"  

print(" LOGIN BIOSKOP XX1")

batasLogin = 3

for percobaan in range(batasLogin):
    username = input("Masukkan Username: ")
    password = input("Masukkan Password: ")

    if username == usernameAkun and password == passwordAkun:
        print("Login berhasil Selamat datang di Bioskop XX1")
        break
    else:
        sisa = batasLogin - (percobaan + 1)
        if batasLogin > 0:
            print(f"Login gagal! Sisa percobaan: {sisa}")
        else:
            print("Anda telah gagal login sebanyak 3 kali. Program berhenti.")
            exit()

while True:
    print(" MENU PEMBELIAN TIKET BIOSKOP XX1")
    print("1. Tiket Reguler  (Rp 50.000)")
    print("2. Tiket VIP      (Rp 100.000)")
    print("3. Tiket VVIP     (Rp 150.000)")
    print("4. Keluar")
    
    pilihan = input("Pilih jenis tiket (1-4): ")

    if pilihan == "1":
        jenis = "Reguler"
        harga = 50000
    elif pilihan == "2":
        jenis = "VIP"
        harga = 100000
    elif pilihan == "3":
        jenis = "VVIP"
        harga = 150000
    elif pilihan == "4":
        print("Terima kasih telah menggunakan layanan Bioskop XX1")
        break
    else:
        print("Pilihan tidak valid!")
        continue

    jumlah = int(input(f"Masukkan jumlah tiket {jenis}: "))

    if jumlah:
        jumlah = int(jumlah)
        if jumlah <= 0:
            print("Jumlah tiket harus lebih dari 0!")
            continue
    else:
        print("Input harus berupa angka! Silakan coba lagi.")
        continue

    total = 0
    for i in range(jumlah):
        total += harga

    if total >= 300000:
        potongan = total * 0.12
        total -= potongan
        print(f" mendapat potongan 12% sebesar Rp {potongan:,.0f}")
    elif total >= 200000:
        potongan = total * 0.08
        total -= potongan
        print(f" mendapat potongan 8% sebesar Rp {potongan:,.0f}")
    elif total >= 150000:
        print("Selamat Anda mendapat Poster Film Eksklusif.")
    else:
        print("\nTidak ada potongan atau bonus.")

    print(" STRUK PEMBELIAN ")
    print(f"Jenis Tiket  : {jenis}")
    print(f"Jumlah Tiket : {jumlah}")
    print(f"Total Bayar  : Rp {total:,.0f}")
    print("Terima kasih telah membeli tiket di Bioskop XX1!")