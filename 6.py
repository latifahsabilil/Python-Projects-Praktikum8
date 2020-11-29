def sortStringByChar(namabuah):
    namabuah.sort(reverse=True, key=len)
    return namabuah
urutan = ['apel', 'rambutan', 'jeruk']
print(sortStringByChar(urutan))
