from django.db import models



class Barang(models.Model):
     nama_barang    = models.CharField(max_length=255)
     quantity       = models.IntegerField()
     stok_minimal = models.IntegerField(default=5)
     create_at      = models.DateTimeField(auto_now_add=True)
     update_at      = models.DateTimeField(auto_now=True)


     def __str__(self):
          return f"{self.id}. {self.nama_barang}"
     

class Pembelian(models.Model):
    barang = models.ForeignKey('Barang', on_delete=models.CASCADE)
    jumlah = models.PositiveIntegerField()
    tanggal = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.barang.nama_barang} - {self.jumlah}"
    

class Penjualan(models.Model):
    barang = models.ForeignKey(Barang, on_delete=models.CASCADE)
    jumlah = models.PositiveIntegerField()
    tanggal = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Jual: {self.barang.nama_barang} - {self.jumlah}"

