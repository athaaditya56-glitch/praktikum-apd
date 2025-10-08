namaAkun = "Aditya nur atha"
nimAkun = "2509106082"

nama = input("Masukkan Nama: ")
nim = input("Masukkan NIM: ")

if nama == namaAkun and nim == nimAkun:
    print("LOGIN BERHASIL")

    print("Opsi Paket Langganan:")
    print("1. Bronze: Biaya administrasi 1%, akses dasar ke lagu-lagu populer.")
    print("2. Silver: Biaya administrasi 3%, akses lagu premium dan playlist kustom.")
    print("3. Gold: Biaya administrasi 5%, akses lagu premium, playlist kustom, dan mode offline.")
    print("4. Platinum: Biaya administrasi 7%, akses semua fitur, playlist kustom, mode offline, dan konten eksklusif artis.")
    pilihan = input("Pilih paket (1/2/3/4): ")

    biayaLangganan = 1500000
    paket = ""
    totalBayar =  0
    keuntungan = ""

    if pilihan == "1":
        biayaAdmin = 1/100
        totalBayar = biayaLangganan + (biayaLangganan * biayaAdmin)
        keuntungan = "Akses dasar ke lagu-lagu populer."
        paket = "Bronze"

    elif pilihan == "2":
        biayaAdmin = 3/100
        totalBayar = biayaLangganan + (biayaLangganan * biayaAdmin)
        keuntungan  = "Akses lagu premium dan playlist kustom."
        paket = "Silver"

    elif pilihan == "3":
        biayaAdmin = 5/100
        totalBayar = biayaLangganan + (biayaLangganan * biayaAdmin)
        keuntungan  = "Akses lagu premium, playlist kustom, dan mode offline."
        paket = "Gold"

    elif pilihan == "4":
        biayaAdmin = 7/100
        totalBayar = biayaLangganan + (biayaLangganan * biayaAdmin)
        keuntungan  = "Akses semua fitur, playlist kustom, mode offline, dan konten eksklusif artis."
        paket = "Platinum"

    else:
        print("ga ada pilihannya bro!")
        exit()

    print(f"Paket yang dipilih : {paket}")
    print(f"Biaya Langganan    : Rp {biayaLangganan:,}")
    print(f"Total Bayar        : Rp {totalBayar:,}")
    print(f"Keuntungan Paket   : {keuntungan}")

else:
    print("LOGIN GAGAL,NIM ATAU Namanya salah bro!")
