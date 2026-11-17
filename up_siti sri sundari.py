print("===================================")
print("     APLIKASI PEMESANAN TIKET")
print("             BIOSKOP")
print("===================================")

while True:
    # 1. Input nama pelanggan
    nama = input("\nMasukkan nama pelanggan: ")

    # 2. Input jenis dan jumlah tiket
    print("\nJenis Tiket:")
    print("1. Reguler  - Rp35.000")
    print("2. VIP      - Rp50.000")
    print("3. Premium  - Rp75.000")

    jenis = input("Pilih jenis tiket: ").lower()
    jumlah = int(input("Masukkan jumlah tiket: "))

    # 3. Menentukan harga tiket
    if jenis == "reguler":
        harga = 35000
    elif jenis == "vip":
        harga = 50000
    elif jenis == "premium":
        harga = 75000
    else:
        print("Jenis tiket tidak tersedia!")
        continue

    # 4. Menghitung total harga
    total = harga * jumlah

    # 5. Mengecek diskon
    if jumlah > 3:
        diskon = total * 10 / 100
    else:
        diskon = 0

    # 6. Menghitung total pembayaran
    bayar = total - diskon

    # 7. Menampilkan struk pembayaran
    print("\n===================================")
    print("          STRUK PEMBAYARAN")
    print("===================================")
    print("Nama Pelanggan :", nama)
    print("Jenis Tiket    :", jenis.upper())
    print("Harga Tiket    : Rp", harga)
    print("Jumlah Tiket   :", jumlah)
    print("Total Harga    : Rp", total)
    print("Diskon         : Rp", int(diskon))
    print("Total Bayar    : Rp", int(bayar))
    print("===================================")
    print("       TERIMA KASIH!")
    print("===================================")

    # 8. Proses berulang
    lagi = input("\nApakah ingin melayani pelanggan lain? (ya/tidak): ")

    if lagi.lower() != "ya":
        print("\nProgram selesai. Terima kasih!")
        break