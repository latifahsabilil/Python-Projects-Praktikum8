#MENU_AWAL
sayur = ('bayam', 'kangkung', 'wortel', 'selada')
print('Menu : ')
A = 'A. = Tambah data sayur'
B = 'B. = Hapus data sayur'
C = 'C. = Tampilkan data sayur'
print(A)
print(B)
print(C)

#MENGINPUT PILIHAN
pilihan = input('Pilihan anda : ')
if (pilihan == 'A'):
    print(sayur)
    sayur_tamb = list(sayur)
    tambahan = input('Sayur yang ditambahkan : ')
    sayur_tamb.append(tambahan)
    sayur_tamb_2 = tuple(sayur_tamb)
    print(sayur_tamb_2)
elif (pilihan == 'B'):
    print(sayur)
    sayur_hps = list(sayur)
    hapus = input('Sayur yang dihapus : ')
    sayur_hps.remove(hapus)
    sayur_hps_2 = tuple(sayur_hps)
    print(sayur_hps_2)
elif (pilihan == 'C'):
    print(sayur)
