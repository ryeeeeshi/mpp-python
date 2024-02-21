# pembeli = input("Nama Pembeli:")
# no_hp = input("NO. HP:")
# jurusan=input("kota tujuan [SBY/BALI/LMP]:")

# if jurusan=="SBY":
#     nama_jurusan="Surabaya"
#     harga=300000
# elif jurusan=="BALI":
#     nama_jurusan="Bali"
#     harga=350000
# else :
#     nama_jurusan="Lampung"
#     harga=500000

# jumlah=int(input("Jumlah Beli:"))

# if jumlah >=3:
#     potong_harga=(jumlah*harga)*0.1
# else:
#     potong_harga=0

# total= (jumlah*harga)-potong_harga

# print("\n------>penjualan tiket bus<------")
# print("|                                   |")
# print("|                                   |")
# print("|          Nama Pembeli :"+str(pembeli))
# print("|         No. Handphone :"+str(no_hp))
# print("|  Kode Jurusan yang dipilih :"+str(jurusan))
# print("|      Nama Kota Tujuan :"+str(nama_jurusan))
# print("|            Harga :",+(harga))
# print("|        Jumlah Beli :",+(jumlah))
# print("|                                   |")
# print("|                                   |")
# print("|-----------------------------------|")
# print("potongan yang didapat : ",+int(potong_harga))
# print("Total Bayar   : ",+int(total))
# print("<-------- Terimakasih -------->\n")











# Inisialisasi list penumpang
penumpang = []
# Program utama
while True:
    print("\nMenu Manajemen Angkot:")
    print("1. Tambah Penumpang")
    print("2. Penumpang Turun")
    print("3. Cetak Daftar Penumpang")
    print("4. Keluar")
    
    pilihan = input("Pilih menu (1/2/3/4): ")
    
    if pilihan == '1':
        nama = input("Masukkan nama penumpang yang ingin ditambahkan: ")
        if nama not in penumpang:
            penumpang.append(nama)
            print(f"Penumpang {nama} telah ditambahkan.")
        else:
            print(f"Penumpang {nama} sudah ada dalam daftar.")
    elif pilihan == '2':
        nama = input("Masukkan nama penumpang yang ingin turun: ")
        if nama in penumpang:
            penumpang.remove(nama)
            print(f"Penumpang {nama} telah turun dari angkutan.")
        else:
            print(f"Penumpang {nama} tidak ada dalam daftar.")
    elif pilihan == '3':
        if not penumpang:
            print("Tidak ada penumpang dalam daftar.")
        else:
            print("Daftar Penumpang:")
            for nama in penumpang:
                print(nama)
    elif pilihan == '4':
        print("Terima kasih telah menggunakan aplikasi Manajemen Angkutan.")
        break
    else:
        print("Pilihan tidak valid. Silakan pilih menu yang benar.")

