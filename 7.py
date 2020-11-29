def palingMahal(buah):
    data = list(buah.values())
    data2 = tuple(buah.keys())
    i = max(data)
    a = data.index(i)
    print(data2[a])
buah = {'apel' : 5000, 'jeruk' : 8500, 'mangga' : 7800, 'duku' : 6500}
palingMahal(buah)
