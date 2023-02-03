from django.contrib import admin

from .models import Barang, jenis
from .models import pakaian,jeniss
from .models import kaoskaki,jeniskk

class kolomBarang(admin.ModelAdmin):
    list_display = ['kodebrg','nama','stok','harga','jenis_id']
    search_fields = ['kodebrg','nama']
    list_filter = ('jenis_id',)
    list_per_page = 3



admin.site.register(Barang,kolomBarang)
admin.site.register(jenis)

class kolompakaian(admin.ModelAdmin):
    list_display = ['kodepakaian','nama','stok','harga','jeniss_id']
    search_fields = ['kodepakaian','nama']
    list_filter = ('jeniss_id',)
    list_per_page = 3

admin.site.register(pakaian,kolompakaian)
admin.site.register(jeniss)

class kolomkaoskaki(admin.ModelAdmin):
    list_display = ['kodekaoskaki','nama','stok','harga','jeniskk_id']
    search_fields = ['kodekaoskaki','nama']
    list_filter = ('jeniskk_id',)
    list_per_page = 3

admin.site.register(kaoskaki,kolomkaoskaki)
admin.site.register(jeniskk)