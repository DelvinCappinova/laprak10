def files(nama_file):
    with open(nama_file, 'r') as file:
        huruf_unik = []

        for baris in file:
            kata2 = baris.strip().split(' ')

            for kata in kata2:
                if kata not in huruf_unik:
                    huruf_unik.append(kata)

    return huruf_unik

huruf_unik = files('link txt (saya bingung caranya :D)')
print(huruf_unik)