Daftar_kontak = {
    "nama" : "Suhaila",
    "telp" : "085211041000",
}
x = int(input("Pilih Menu : "))
kontak_list = []

if x == 1 :
    print("===DAFTAR KONTAK===")
    print(Daftar_kontak["nama"])
    print(Daftar_kontak["telp"])
elif x == 2 :
    for i in range(2):
        nama = input("Masukkan Nama Kontak : ")
        telp = input("Masukkan Nomor HP : ")
        data = {
            "nama" : nama,
            "telp" : telp,
        }
        kontak_list.append(data)
    for i in kontak_list:
        print("Nama Kontak : ",i["nama"])
        print("No HP : ",i["telp"])
    print("Kontak berhasil ditambahkan")
elif x == 3 :
    print("Program selesai sampai jumpa!")
else:
    print("Menu tidak tersedia")