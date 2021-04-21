x = int(input("Masukkan x : "))
y = int(input("Masukkan y : "))

if x > y :
    print("x lebih besar dari y")
elif x < y:
    print("x kurang dari y")
elif x == y:
    print("x sama dengan y")
else:
    print("salah input !")

tanya = input("Mau makan ? ")
if tanya == "ya" or tanya == "YA":
    print("mau makan apa ?")
elif tanya == "tidak":
    print("oke kalau gitu mau cemilan ?")
else:
    print("oke")