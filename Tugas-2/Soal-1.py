Daftar_kontak = {
    "Nama" : "Suhaila",
    "No_Hp" : "085211041000",
    "Nama" : "Ayla",
    "No_Hp" : "085215256556",
}
x = int(input("Pilih Menu : "))
pelanggan_list = []

if x == 1 :
    print("DAFTAR KONTAK")
    print("Nama Kontak :",(Daftar_kontak["Nama"]))
    print("No HP :",(Daftar_kontak["No_Hp"]))
elif x == 2 :
    for i in range(1):
    nama = input("Masukkan Nama Kontak : ")
    telp = input("Masukkan Nomor HP : ")
    data = {
        "Nama" : nama,
        "No_Hp" : telp,
    }
    pelanggan_list.append(data)
    print("Kontak berhasil ditambahkan")