for i in range(5):
    print(i)

print("=========")

for i in range(5):
    # berikan kondisi sesuai keinginan
    if  i == 1 or i == 3:
        continue
    print(i)

# simulasikan
# 1
# 2
# 3 => perulangan tidak dijalankan alias di skip
# 4
# 5