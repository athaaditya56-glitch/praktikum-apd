
barang = [
    ["Raket", 2000000, 10],
    ["Shuttlecock", 130000, 20],
    ["Sepatu", 3000000, 5]
]

while True:
    print("MENU TOKO BULUTANGKIS")
    print("1. Lihat Barang")
    print("2. Tambah Barang")
    print("3. Ubah Barang")
    print("4. Hapus Barang")
    print("5. Keluar")

    pilih = input("Pilih menu: ")

    # READ
    if pilih == "1":
        print("DAFTAR BARANG")
        if barang == []:
            print("Belum ada barang.")
        else:
            nomor = 1
            i = 0
            for _ in barang:
                print(f"{nomor}. {barang[i][0]}  Harga: Rp{barang[i][1]}  Stok: {barang[i][2]}")
                nomor += 1
                i += 1

    # CREATE 
    elif pilih == "2":
        print("TAMBAH BARANG")
        nama = input("Nama barang: ")
        harga = input("Harga: ")
        stok = input("Stok: ")

        if harga.isdigit() and stok.isdigit():
            barang.append([nama, int(harga), int(stok)])
            print("Barang berhasil ditambahkan.")
        else:
            print("Harga dan stok harus berupa angka.")

    # UPDATE 
    elif pilih == "3":
        print("UBAH BARANG")
        if barang == []:
            print("Belum ada barang.")
        else:
            nomor = 1
            i = 0
            for _ in barang:
                print(f"{nomor}. {barang[i][0]}  Harga: Rp{barang[i][1]}  Stok: {barang[i][2]}")
                nomor += 1
                i += 1

            ubah = input("Masukkan nomor barang yang ingin diubah: ")
            if ubah.isdigit():
                nomor_ubah = int(ubah) - 1
                hitung = 0
                valid = False
                for _ in barang:
                    if hitung == nomor_ubah:
                        valid = True
                        break
                    hitung += 1

                if valid:
                    nama_baru = input("Nama baru: ")
                    harga_baru = input("Harga baru: ")
                    stok_baru = input("Stok baru: ")

                    if harga_baru.isdigit() and stok_baru.isdigit():
                        data_lama = barang[nomor_ubah]
                        del barang[nomor_ubah]
                        barang.append([nama_baru, int(harga_baru), int(stok_baru)])
                        print("Barang berhasil diubah .")
                    else:
                        print("Harga dan stok harus berupa angka.")
                else:
                    print("Nomor tidak valid.")
            else:
                print("Input harus angka.")

    # DELETE 
    elif pilih == "4":
        print("HAPUS BARANG")
        if barang == []:
            print("Belum ada barang.")
        else:
            nomor = 1
            i = 0
            for _ in barang:
                print(f"{nomor}. {barang[i][0]}  Harga: Rp{barang[i][1]}  Stok: {barang[i][2]}")
                nomor += 1
                i += 1

            hapus = input("Masukkan nomor barang yang ingin dihapus: ")
            if hapus.isdigit():
                nomor_hapus = int(hapus) - 1
                hitung = 0
                valid = False
                for _ in barang:
                    if hitung == nomor_hapus:
                        valid = True
                        break
                    hitung += 1

                if valid:
                    del barang[nomor_hapus]
                    print("Barang berhasil dihapus.")
                else:
                    print("Nomor tidak valid.")
            else:
                print("Input harus angka.")

    # EXIT
    elif pilih == "5":
        print("Terima kasih telah menggunakan program ini.")
        break

    else:
        print("Pilihan tidak ada dalam menu.")
