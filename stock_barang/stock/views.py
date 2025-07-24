from django.shortcuts import render, redirect, get_object_or_404
from django.views.generic.base import TemplateView , RedirectView, View
from .models import Barang,Pembelian,Penjualan
from .forms import StockForm,PembelianForm,PenjualanForm




def index (request):
     all_data = Barang.objects.all()
     context ={
          'title'        : 'BARANG',
          'semua_data'   : all_data
     }

     return render (request,"stock/index.html",context)

def detail (request):
     all_data = Barang.objects.all()
     context ={
          'title'        : 'BARANG',
          'semua_data'   : all_data
     }

     return render (request,"stock/detail.html",context)

def create(request):
    form = StockForm(request.POST or None)

    if request.method == 'POST':
        if form.is_valid():
            form.save()
            return redirect('stock:index')

    context = {
        'title': 'Tambah Barang',
        'data_form': form,
    }
    return render(request, "stock/create.html", context)


def update(request, id):
    barang = get_object_or_404(Barang, id=id)
    form = StockForm(request.POST or None, instance=barang)

    if request.method == 'POST':
        if form.is_valid():
            form.save()
            return redirect('stock:index')

    context = {
        'title': 'Update Barang',
        'data_form': form,
    }
    return render(request, 'stock/update.html', context)


def delete_barang(request, id):
    
    barang = get_object_or_404(Barang, id=id)
    barang.delete()

    return redirect('stock:index')



def pembelian(request, id):
    barang = get_object_or_404(Barang, id=id)
    form = PembelianForm(request.POST or None)

    if request.method == 'POST':
        if form.is_valid():
            jumlah = form.cleaned_data['jumlah']

            #  Cek stok sekarang
            if barang.quantity == 0 and jumlah < 5:
                form.add_error('jumlah', "Stok kosong. Minimal pembelian adalah 5 unit.")
            else:
                #  Tambah stok
                barang.quantity += jumlah
                barang.save()

                #  Simpan riwayat pembelian
                Pembelian.objects.create(barang=barang, jumlah=jumlah)

                return redirect('stock:index')

    context = {
        'title': f'Pembelian {barang.nama_barang}',
        'barang': barang,
        'form': form,
    }
    return render(request, 'stock/pembelian.html', context)



def penjualan(request, id):
    barang = get_object_or_404(Barang, id=id)
    form = PenjualanForm(request.POST or None)

    if request.method == 'POST':
        if form.is_valid():
            jumlah = form.cleaned_data['jumlah']

            if jumlah > barang.quantity:
                form.add_error('jumlah', f"Stok tidak mencukupi. Tersisa: {barang.quantity}")
            
            elif barang.quantity - jumlah < 5:
                form.add_error(None, f"Penjualan ditolak. Minimal stok harus tersisa 5. Saat ini: {barang.quantity}")
            
            else:
                # Kurangi stok
                barang.quantity -= jumlah
                barang.save()

                # Simpan penjualan
                Penjualan.objects.create(barang=barang, jumlah=jumlah)

                return redirect('stock:index')

    return render(request, 'stock/penjualan.html', {
        'barang': barang,
        'form': form,
        'title': f"Penjualan {barang.nama_barang}"
    })





def riwayat_barang(request):
    data_pembelian = Pembelian.objects.all()
    data_penjualan = Penjualan.objects.all()

    context = {
        'data_pembelian': data_pembelian,
        'data_penjualan': data_penjualan,
        'title': 'Riwayat Transaksi Barang'
    }
    return render(request, 'stock/riwayat.html', context)