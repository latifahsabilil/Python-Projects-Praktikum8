jawab = 'ya'
i = 0
while True :
    i += 1
    nama_mhs = input('Nama Mahasiswa : ')
    mylist = list(nama_mhs)
    print(nama_mhs, '(', len(mylist), 'karakter)')
    tanya = input('Tambah lagi? (ya/tidak) : ')
    if (tanya == 'tidak'):
        break
