nama_pelanggan = input("masukkan nama pelanggan\t\t : ")
produk = input("Pilihan\t\t : ")
if (produk == "Kipas angin"):
    harga = 1000000
    print ("Harga produk\t\t\t\t : %i" % (harga))
elif (produk == "tv"):
    harga = 2000000
    print ("Harga produk: %i" % (harga))
elif (produk == "mesin cuci"):
    harga = 3000000
    print ("Harga produk: %i" % (harga))
elif (produk == "ac"):
    harga = 4000000
    print ("Harga produk: %i" % (harga))
else: 
    harga = 5000000
    print ("Harga produk: %i" % (harga))

jumlah_beli = int(input("Jumlah barang: "))
harga_kotor = harga * jumlah_beli
print("harga_kotor: %i" % (harga_kotor))
if (produk == "kulkas" and jumlah_beli >= 5):
    diskon = 0.20 * harga_kotor

elif (produk == "ac" and jumlah_beli >= 3):
      diskon = 0.10 * harga_kotor
else:
    diskon = 0.05 * harga_kotor

ppn = harga_kotor - diskon * 0.10
print("PPN: %i " % (ppn))
harga_bersih = harga_kotor - diskon + ppn
print("harga bersih: %i" % (harga_bersih))