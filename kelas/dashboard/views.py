from django.shortcuts import render, redirect
from dashboard.forms import FormBarang, Formpakaian, Formkaoskaki
from dashboard.models import Barang, pakaian, kaoskaki
from django.contrib import messages
from dashboard.views import *

def dashboard(request):
    title= "Dashboard"
    konteks = {
        'titlenya': title,
    }
    return render(request, 'dashboard.html', konteks)

def Barang_View(request):
    barangs = Barang.objects.all()

    konteks = {
        'barangs':barangs,
    }

    return render (request, 'tampil_brg.html', konteks)

def pakaian_View(request):
    pakaians = pakaian.objects.all()

    konteks = {
        'pakaians':pakaians,
    }

    return render (request, 'tampil_pakaian.html', konteks)

def kaoskaki_View(request):
    kaoskakis = kaoskaki.objects.all()

    konteks = {
        'kaoskakis':kaoskakis,
    }

    return render (request, 'tampil_kaoskaki.html', konteks)

def cart(request):
    title= "Cart"
    konteks = {
        'titlenya': title,
    }
    return render(request, 'cart.html', konteks)


def category(request):
    title= "Category"
    konteks = {
        'titlenya': title,
    }
    return render(request, 'category.html', konteks)

def wish(request):
    title= "Wish"
    konteks = {
        'titlenya': title,
    }
    return render(request, 'wish.html', konteks)

def tambah_barang(request):
    if request.POST:
        form = FormBarang(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request,"Data Berhasil Ditambahkan")
            form = FormBarang()
            konteks = {
                'form' : form,
            }
            return render(request, 'tambah_barang.html', konteks)
    else:
        form=FormBarang()
        konteks = {
            'form' : form,
        }
    return render(request, 'tambah_barang.html', konteks)

def ubah_brg(request,id_barang):
    barangs=Barang.objects.get(id=id_barang)
    if request.POST:
        form=FormBarang(request.POST,instance=barangs)
        if form.is_valid():
            form.save()
            messages.success(request,"Data Berhasil di Ubah")
            return redirect('ubah_brg', id_barang=id_barang)
    else:
        form=FormBarang(instance=barangs)
        konteks = {
            'form':form,
            'barangs':barangs
        }
    return render(request,'ubah_brg.html',konteks)

def hapus_brg(request, id_barang):
    barangs=Barang.objects.filter(id=id_barang)
    barangs.delete()
    messages.success(request, "Data Terhapus")
    return redirect('/Vbrg')

##pakaian
def tambah_pakaian(request):
    if request.POST:
        form=Formpakaian(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request,"Data Berhasil Ditambahin")
            form = Formpakaian()
            konteks = {
                'form': form,
            }
            return render(request,'tambah_pakaian.html',konteks)
    else:
        form=Formpakaian()
        konteks = {
            'form': form,
        }
    return render(request,'tambah_pakaian.html', konteks)

def ubah_pakaian(request, id_pakaian):
    pakaians=pakaian.objects.get(id=id_pakaian)
    if request.POST:
        form=Formpakaian(request.POST, instance=pakaians)
        if form.is_valid():
            form.save()
            messages.success(request,"Data Berhasil diubah")
            return redirect('ubah_pakaian', id_pakaian=id_pakaian)
    else:
        form=Formpakaian(instance=pakaians)
        konteks = {
            'form' : form,
            'pakaians' : pakaians
        }
    return render(request,'ubah_pakaian.html', konteks)
    
def hapus_pakaian(request, id_pakaian):
    pakaians=pakaian.objects.filter(id=id_pakaian)
    pakaians.delete()
    messages.success(request, "Data Terhapus")
    return redirect('/tampil_pakaian')


##pakaian
def tambah_kaoskaki(request):
    if request.POST:
        form=Formkaoskaki(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request,"Data Berhasil Ditambahin")
            form = Formkaoskaki()
            konteks = {
                'form': form,
            }
            return render(request,'tambah_kaoskaki.html',konteks)
    else:
        form=Formkaoskaki()
        konteks = {
            'form': form,
        }
    return render(request,'tambah_kaoskaki.html', konteks)

def ubah_kaoskaki(request, id_kaoskaki):
    kaoskakis=kaoskaki.objects.get(id=id_kaoskaki)
    if request.POST:
        form=Formkaoskaki(request.POST, instance=kaoskakis)
        if form.is_valid():
            form.save()
            messages.success(request,"Data Berhasil diubah")
            return redirect('ubah_kaoskaki', id_kaoskaki=id_kaoskaki)
    else:
        form=Formkaoskaki(instance=kaoskakis)
        konteks = {
            'form' : form,
            'kaoskakis' : kaoskakis
        }
    return render(request,'ubah_kaoskaki.html', konteks)
   
def hapus_kaoskaki(request, id_kaoskaki):
    kaoskakis=kaoskaki.objects.filter(id=id_kaoskaki)
    kaoskakis.delete()
    messages.success(request, "Data Terhapus")
    return redirect('/tampil_kaoskaki')