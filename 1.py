def listangka(input_angka):
    listku = sorted(input_angka, reverse=True)
    return listku[:3]
angka = [23, 43, 11, 2, 34, 345, 756, 903]
print(listangka(angka))