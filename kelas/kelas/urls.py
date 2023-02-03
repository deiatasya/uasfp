from django.contrib import admin
from django.urls import path
from django.http import HttpResponse
from django.shortcuts import render
from dashboard.views import dashboard, cart, category, hapus_brg, ubah_brg, ubah_pakaian, wish, tambah_barang, tambah_pakaian, hapus_pakaian, pakaian_View, Barang_View, kaoskaki_View, tambah_kaoskaki, ubah_kaoskaki, hapus_kaoskaki


# def coba1(request):
#     return HttpResponse('Selamat Datang !')

def coba2(request):
    title= "Home"
    konteks = {
        'titlenya': title,
    }
    return render(request, 'home.html', {'navbar':'home'})

def cart(request):
    title= "Cart"
    konteks = {
        'titlenya': title,
    }
    return render(request, 'cart.html', {'navbar':'cart'})

def wish(request):
    title= "Wish"
    konteks = {
        'titlenya': title,
    }
    return render(request, 'wish.html', {'navbar':'wish'})

urlpatterns = [
    path('admin/', admin.site.urls),
    # path('', coba1),
    path('', coba2),
    path('dashboard/', dashboard),
    path('category/', category),
    path('cart/', cart),
    path('wish/', wish),
    path('tambah_barang/', tambah_barang),
    path('tambah_pakaian/', tambah_pakaian),
    path('tambah_kaoskaki/', tambah_kaoskaki),
    path('Vbrg/', Barang_View),
    path('tampil_pakaian/', pakaian_View),
    path('tampil_kaoskaki/', kaoskaki_View),
    path('ubah/<int:id_barang>',ubah_brg,name='ubah_brg'),
    path('hapus/<int:id_barang>',hapus_brg,name='hapus_brg'),
    path('ubahpakaian/<int:id_pakaian>',ubah_pakaian,name='ubah_pakaian'),
    path('hapuskaoskaki/<int:id_kaoskaki>',hapus_kaoskaki,name='hapus_kaoskaki'),
    path('ubahkaoskaki/<int:id_kaoskaki>', ubah_kaoskaki,name='ubah_kaoskaki'),
    path('hapuspakaian/<int:id_pakaian>',hapus_pakaian,name='hapus_pakaian')

   
]
