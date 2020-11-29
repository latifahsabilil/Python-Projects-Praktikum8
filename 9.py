buah = {'apel' : 5000, 'jeruk' : 8500, 'mangga' : 7800, 'duku' : 6500}
nama_buah = list(buah)
harga_buah = list(buah.values())

#INPUT BUAH DAN BANYAKNYA BUAH YANG DIBELI
buah_beli = input('Nama buah yang dibeli : ')
kg_beli = int(input('Berapa Kg             : '))
print('---------------------------------')

#HITUNG TOTAL YANG DIBELI
indx = nama_buah.index(buah_beli)
harga_beli = harga_buah[indx] * kg_beli
print('Total harga           : ',harga_beli)

