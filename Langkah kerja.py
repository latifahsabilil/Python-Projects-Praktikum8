#Membuat list a dan b
a = [1, 5, 6, 3, 6, 9, 11, 20, 12]
b = [7, 4, 5, 6, 7, 1, 12, 5, 9]
print(a)
print(b)

#Menyisipkan nilai ke indeks
a.insert(3, 10)
b.insert(2, 15)
print(a)
print(b)

#Menyisipkan nilai ke indeks terakhir
a.append(4)
b.append(8)
print(a)
print(b)

#Melakukan sort secara ascending
a.sort()
b.sort()
print(a)
print(b)

#Membuat List c dan List d
c = a[0:7]
d = b[2:9]

print(c)
print(d)

#Membuat List e
e = []
for i in range (len(c)):
    baru = c[i] + d[i]
    e = e + [baru]
print(e)

#Mengubah List menjadi tuple
e = tuple(e)
print(e)

#Mencari nilai min, max dan jumlahan
nilai_minimum = min(e)
nilai_maksimum = max(e)
jumlahan = sum(e)
print(nilai_minimum, nilai_maksimum, jumlahan)

#Membuat string
myString = "python adalah bahasa pemrograman yang menyenangkan"

#Mengetahui karakter
karakter = set(myString)
print(karakter)

#Mengurutkan alphabet
myList = list(karakter)
myList.sort()
print(myList)
