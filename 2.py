print("Masukkan deretan angka, akhiri dengan 'done'.")
angka = []
while True:
    input_angka = input("Masukkan angka: ")
    if input_angka.lower() == 'done':
        break
    else:
        angka.copyappend(int(input_angka))
min = min(angka)
max = max(angka)

print(f"Nilai minimum: {min}")
print(f"Nilai maksimum: {max}")