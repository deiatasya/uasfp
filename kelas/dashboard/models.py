from django.db import models

class jenis(models.Model):
    nama=models.CharField(max_length=50)
    ket=models.TextField()

    def __str__(self):
        return self.nama

class Barang(models.Model):
    kodebrg=models.CharField(max_length=8)
    nama=models.CharField(max_length=50)
    stok=models.IntegerField()
    harga=models.BigIntegerField()
    link_gbr=models.CharField(max_length=150, blank=True)
    timestamp=models.DateTimeField(auto_now_add=True) 
    jenis_id=models.ForeignKey(jenis, on_delete=models.CASCADE, null=True)

    def __str__(self):
        # return self.nama
        return "{} - {} - {}".format(self.kodebrg, self.nama, self.stok)

class jeniss(models.Model):
    nama=models.CharField(max_length=50)
    ket=models.TextField()

    def __str__(self):
        return self.nama

class pakaian(models.Model):
    kodepakaian=models.CharField(max_length=8)
    nama=models.CharField(max_length=50)
    stok=models.IntegerField()
    harga=models.BigIntegerField()
    link_gbr=models.CharField(max_length=150, blank=True)
    timestamp=models.DateTimeField(auto_now_add=True) 
    jeniss_id=models.ForeignKey(jeniss, on_delete=models.CASCADE, null=True)

    def __str__(self):
        # return self.nama
        return "{} - {} - {}".format(self.kodepkn, self.nama, self.stok)


class jeniskk(models.Model):
    nama=models.CharField(max_length=50)
    ket=models.TextField()

    def __str__(self):
        return self.nama

class kaoskaki(models.Model):
    kodekaoskaki=models.CharField(max_length=8)
    nama=models.CharField(max_length=50)
    stok=models.IntegerField()
    harga=models.BigIntegerField()
    link_gbr=models.CharField(max_length=150, blank=True)
    timestamp=models.DateTimeField(auto_now_add=True) 
    jeniskk_id=models.ForeignKey(jeniskk, on_delete=models.CASCADE, null=True)

    def __str__(self):
        # return self.nama
        return "{} - {} - {}".format(self.kodekaoskaki, self.nama, self.stok)
