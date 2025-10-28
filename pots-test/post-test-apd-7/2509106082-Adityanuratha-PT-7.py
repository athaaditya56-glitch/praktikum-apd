#  VARIABEL GLOBAL
users = {
    "si_admin": {"password": "123", "role": "admin"},
    "abang1": {"password": "aaa", "role": "pengguna"}
}

barang = {
    1: {"nama": "Raket", "harga": 2000000, "stok": 10},
    2: {"nama": "Shuttlecock", "harga": 130000, "stok": 20},
    3: {"nama": "Sepatu", "harga": 3000000, "stok": 5}
}

role = ""  

print(" SISTEM LOGIN TOKO BULUTANGKIS ")


# PARAMETER 
def login(username, password):
    global role
    try:
        if username in users and users[username]["password"] == password:
            role = users[username]["role"]
            print(f"Selamat datang, {username}! (Role: {role})")
            return True
        else:
            raise ValueError("Password atau username salah bang!silakan coba login kembali.")
    except ValueError as e:
        print(e)
        return False
    finally:
        print("Proses login selesai.")


# TANPA PARAMETER 
def tampilkan_barang():
    try:
        if not barang:
            print("Belum ada barang.")
        else:
            print(" DAFTAR BARANG ")
            for id_barang, data in barang.items():
                print(f"{id_barang}. {data['nama']} - Harga: Rp{data['harga']} - Stok: {data['stok']}")
    except Exception as e:
        print("Terjadi kesalahan saat menampilkan barang:", e)
    finally:
        print()


# PARAMETER
def hapus_barang_param(id_barang):
    try:
        if id_barang in barang:
            del barang[id_barang]
            print("Barang berhasil dihapus.")
            return True
        else:
            raise KeyError("Nomor tidak valid.")
    except KeyError as e:
        print("Error:", e)
        return False
    finally:
        print()


# TANPA PARAMETER
def jumlah_barang():
    try:
        total = len(barang)
        print(f"Jumlah total barang saat ini: {total}")
    except Exception as e:
        print("Terjadi kesalahan saat menghitung barang:", e)
    finally:
        print()


#  PROSEDUR 
def tambah_barang():
    try:
        nama = input("Nama barang: ")
        harga = input("Harga: ")
        stok = input("Stok: ")
        # Variabel lokal: nama, harga, stok, id_baru, data_baru
        if harga.isdigit() and stok.isdigit():
            id_baru = max(barang.keys()) + 1 if barang else 1
            data_baru = {"nama": nama, "harga": int(harga), "stok": int(stok)}
            barang[id_baru] = data_baru
            print("Barang berhasil ditambahkan.")
        else:
            raise ValueError("Harga dan stok harus berupa angka.")
    except ValueError as e:
        print("Error:", e)
    finally:
        print()


def ubah_barang():
    try:
        if not barang:
            print("Belum ada barang.")
        else:
            print(" UBAH BARANG ")
            for id_barang, data in barang.items():
                print(f"{id_barang}. {data['nama']} - Harga: Rp{data['harga']} - Stok: {data['stok']}")

            ubah = input("Masukkan nomor barang yang ingin diubah: ")
            if ubah.isdigit() and int(ubah) in barang:
                id_barang = int(ubah)
                nama_baru = input("Nama baru: ")
                harga_baru = input("Harga baru: ")
                stok_baru = input("Stok baru: ")

                if harga_baru.isdigit() and stok_baru.isdigit():
                    barang[id_barang]["nama"] = nama_baru
                    barang[id_barang]["harga"] = int(harga_baru)
                    barang[id_barang]["stok"] = int(stok_baru)
                    print("Barang berhasil diubah.")
                else:
                    raise ValueError("Harga dan stok harus berupa angka.")
            else:
                raise KeyError("Nomor tidak valid.")
    except KeyError as e:
        print("Error:", e)
    except ValueError as e:
        print("Error:", e)
    finally:
        print()


#  PROGRAM UTAMA 
while True:
    try:
        username = input("Masukkan username: ")
        password = input("Masukkan password: ")
        if login(username, password):
            break
    except Exception as e:
        print("Terjadi kesalahan saat login:", e)

#  MENU 
while True:
    print(" MENU TOKO BULUTANGKIS ")
    print("1. Lihat Barang")
    print("2. Tambah Barang")

    if role == "admin":
        print("3. Ubah Barang")
        print("4. Hapus Barang")
        print("5. Lihat Jumlah Barang")
        print("6. Keluar")
    else:
        print("3. Lihat Jumlah Barang")
        print("4. Keluar")

    pilih = input("Pilih menu: ")

    try:
        # READ
        if pilih == "1":
            tampilkan_barang()

        # CREATE
        elif pilih == "2":
            tambah_barang()

        # UPDATE (admin)
        elif pilih == "3" and role == "admin":
            ubah_barang()

        # HAPUS (admin)
        elif pilih == "4" and role == "admin":
            try:
                if not barang:
                    print("Belum ada barang.")
                else:
                    print(" HAPUS BARANG ")
                    for id_barang, data in barang.items():
                        print(f"{id_barang}. {data['nama']} - Harga: Rp{data['harga']} - Stok: {data['stok']}")
                    hapus = input("Masukkan nomor barang yang ingin dihapus: ")

                    if hapus.isdigit():
                        hapus_barang_param(int(hapus))
                    else:
                        raise KeyError("Nomor tidak valid.")
            except KeyError as e:
                print("Error:", e)
            finally:
                print()

        # JUMLAH BARANG
        elif (pilih == "5" and role == "admin") or (pilih == "3" and role == "pengguna"):
            jumlah_barang()

        # EXIT
        elif (pilih == "6" and role == "admin") or (pilih == "4" and role == "pengguna"):
            print("Terima kasih telah menggunakan program ini.")
            break

        else:
            print("Pilihan tidak ada dalam menu.")

    except Exception as e:
        print("Terjadi kesalahan:", e)
