# inputan
input_satu = input(("masukkan kalimat :"))
input_dua = input(("masukkan kata: "))

# proses
input_satu = input_satu.lower().split()
input_dua = input_dua.lower()

total = 0

for i in input_satu:
    if i == input_dua:
        total += 1

# output
print(total)