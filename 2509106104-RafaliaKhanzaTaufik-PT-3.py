nama1 = "Rafalia Khanza Taufik"
nim1 = "104"
uKT = 6000000
print("Masukkan Nama Panjang Anda")
nama = input()
print("Masukkan NIM Anda")
nim = input()
if nama == nama1 and nim == nim1:
    print("Pilih Pembayaran UKT Anda")
    print("1. Lunas (Sekali Bayar): Biaya administrasi 1%")
    print("2. Cicilan 2x per Semester: Biaya administrasi 5%")
    print("3. Cicilan 4x per Semester: Biaya administrasi 8%")
    print("4. Cicilan 6x per Semester: Biaya administrasi 12%")
    print("Pilih Metode Pembayaran Anda")
    pilihan = input()
    if pilihan == "1":
        biayaAdmin = 0.01
        totalBayar = uKT + uKT * biayaAdmin
        print("Total Bayar : Rp" + str(totalBayar))
    else:
        if pilihan == "2":
            biayaAdmin = 0.05
            totalBayar = uKT + uKT * biayaAdmin
            cicilan = totalBayar / 2
            print("Total Bayar : Rp" + str(totalBayar) + " Cicilanya :" + str(cicilan))
        else:
            if pilihan == "3":
                biayaAdmin = 0.08
                totalBayar = uKT + uKT * biayaAdmin
                cicilan = totalBayar / 4
                print("Total Bayar : Rp" + str(totalBayar) + " Cicilanya :" + str(cicilan))
            else:
                if pilihan == "4":
                    biayaAdmin = 0.12
                    totalBayar = uKT + uKT * biayaAdmin
                    cicilan = totalBayar / 6
                    print("Total Bayar : Rp" + str(totalBayar) + " Cicilanya :" + str(cicilan))
    print("Silahkan Melakukan Pembayaran Anda")
else:
    print("Login Gagal")
