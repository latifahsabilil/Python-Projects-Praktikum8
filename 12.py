buah = {'apel' : 5000, 'jeruk' : 8500, 'mangga' : 7800, 'duku' : 6500}
nama_buah = list(buah)
harga_buah = list(buah.values())
hitung = []

print('Menu :')
print('A. Tambah data buah')
print('B. Beli buah')
print('C. Hapus data buah')
pilihMenu = input('Pilihan menu : ')

if pilihMenu == 'A':
    buah_baru = input('Masukkan nama buah : ')
    if buah_baru in buah :
        print('Buah sudah terdapat dalam daftar')
        buah_baru = input('Masukkan nama buah : ')
    harga_baru = int(input('Masukkan harga satuan : '))
    buah[buah_baru] = harga_baru
    print(buah)

elif pilihMenu == 'B':
    while True:
        buah_beli = input('Nama buah yang dibeli : ')
        kg_beli = int(input('Berapa Kg             : '))
        indx = nama_buah.index(buah_beli)
        harga_beli = harga_buah[indx] * kg_beli
        hitung.append(harga_beli)
        print('')
        tanya = input('Beli buah yang lain(y/n)? ')
        print('')
        if tanya == 'y' :
            continue
        elif tanya == 'n' :
            break
        else:
            print('Input salah')
            print('')
            tanya = input('Beli buah yang lain(y/n)? ')
            print('')
    print('---------------------------------')

    #HITUNG TOTAL YANG DIBELI
    harga_beli2 = sum(hitung)
    print('Total harga           : ',harga_beli2)

elif pilihMenu == 'C':
    buah_hapus = input('Masukkan nama buah : ')
    if buah_hapus not in buah :
        print('Nama buah tidak ditemukan')
        buah_hapus = input('Masukkan nama buah : ')
    del buah[buah_hapus]
    print(buah)
