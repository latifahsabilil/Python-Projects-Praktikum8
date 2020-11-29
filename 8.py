buah = {'apel' : 5000, 'jeruk' : 8500, 'mangga' : 7800, 'duku' : 6500}
def rerata_harga(buah):
    hasil = []
    for i in buah :
        rata2 = list(buah.values())
        average = sum(rata2) / len(rata2)
        hasil = [average]
    return hasil
print(rerata_harga(buah))
