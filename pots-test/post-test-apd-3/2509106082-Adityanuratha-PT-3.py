namaAkun = "Aditya nur atha"
nimAkun = "2509106082"
biayaLangganan= 1500000

print(" LOGIN DULU KAWAN ")
nama = input("Masukkan Nama: ")
nim = input("Masukkan NIM: ")

if nama == namaAkun and nim == nimAkun:
    print(" PILIH  LANGGANAN ")
    print("1. Bronze (1% biaya admin)Akses dasar ke lagu-lagu populer")
    print("2. Silver (3% biaya admin)Akses lagu premium dan playlist kustom")
    print("3. Gold (5% biaya admin)Akses lagu premium, playlist kustom, dan mode offline")
    print("4. Platinum (7% biaya admin)Akses semua fitur, playlist kustom, mode offline, dan konten eksklusif artis")

    pilihan = input("Masukkan pilihan  (1-4): ")

    if pilihan == "1":
        biayaAdmin= biayaLangganan* 1/100
        totalBayar= biayaLangganan+ biayaAdmin
        print("pilihan langganan: Bronze")
        print(f"Biaya Langganan   : Rp{biayaLangganan:,}")
        print(f"Biaya Admin (1%)  : Rp{biayaAdmin:,}")
        print(f"Total Bayar       : Rp{totalBayar:,.0f}")
        print("Keuntungan         : Akses dasar ke lagu-lagu populer")

    elif pilihan == "2":
        biayaAdmin= biayaLangganan* 3/100
        totalBayar= biayaLangganan+ biayaAdmin
        print("pilihan langganan: Silver")
        print(f"Biaya Langganan   : Rp{biayaLangganan:,}")
        print(f"Biaya Admin (3%)  : Rp{biayaAdmin:,}")
        print(f"Total Bayar       : Rp{totalBayar:,.0f}")
        print("Keuntungan         : Akses lagu premium dan playlist kustom")

    elif pilihan == "3":
        biayaAdmin= biayaLangganan* 5/100
        totalBayar= biayaLangganan+ biayaAdmin
        print("pilihan langganan: Gold")
        print(f"Biaya Langganan   : Rp{biayaLangganan:,}")
        print(f"Biaya Admin (5%)  : Rp{biayaAdmin:,}")
        print(f"Total Bayar       : Rp{totalBayar:,.0f}")
        print("Keuntungan         : Akses lagu premium, playlist kustom, dan mode offline")

    elif pilihan == "4":
        biayaAdmin= biayaLangganan* 7/100
        totalBayar= biayaLangganan+ biayaAdmin
        print("pilihan langganan: Platinum")
        print(f"Biaya Langganan   : Rp{biayaLangganan:,}")
        print(f"Biaya Admin (7%)  : Rp{biayaAdmin:,}")
        print(f"Total Bayar       : Rp{totalBayar:,.0f} ")
        print("Keuntungan         : Akses semua fitur, playlist kustom, mode offline, dan konten eksklusif artis")

    else:
        print("Pilihannya tidak ada bang!")

else:
    print("Login gagal! Nama atau NIM salah bang!.")