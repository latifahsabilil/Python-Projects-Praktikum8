buah = {'apel' : 5000, 'jeruk' : 8500, 'mangga' : 7800, 'duku' : 6500}
nama_buah = list(buah)
harga_buah = list(buah.values())
hitung = []
#INPUT BUAH DAN BANYAKNYA BUAH YANG DIBELI
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

