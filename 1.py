n = int(input('Masukkan berapa banyak bilangan bulat yang diinginkan : '))
x = 0
bil = []
while (x < n) :
    angka = int(input('Masukkan bilangan bulat: '))
    bil = bil + [angka]
    x += 1
bil.sort(reverse=True)
print(bil)
