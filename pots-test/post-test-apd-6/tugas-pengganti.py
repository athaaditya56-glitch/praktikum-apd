mahasiswa = {
    "11210001": {
        "nama": "jokowididi",
        "kelas": "TI-01", 
        "IPK": 3.75
    },
    "11210002": {
        "nama": "praboro",
        "kelas": "TI-02",
        "IPK": 3.89
    },
    "11210003": {
        "nama": "vladimir udin", 
        "kelas": "TI-01",
        "IPK": 3.45
    }
}


print("=" * 40)
print("        DATA MAHASISWA")
print("=" * 40)

for nim, data in mahasiswa.items():
    print(f"NIM    : {nim}")
    
    for key, value in data.items():
        if key == "nama":
            print(f"Nama   : {value}")
        elif key == "kelas":
            print(f"Kelas  : {value}")
        elif key == "IPK":
            print(f"IPK    : {value}")
    
    print("-" * 40)

print("Total mahasiswa:", len(mahasiswa))