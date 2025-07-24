from django.urls import path
from . import views 

app_name = "stock"

urlpatterns =[
     path ('',views.index, name = 'index'),
     path ('create/',views.create, name = 'create'),
     path ('detail/',views.detail, name = 'detail'),
     path ('update/<int:id>/',views.update, name = 'update'),
     path('delete/<int:id>/', views.delete_barang, name='delete'),
     path('beli/<int:id>/', views.pembelian, name='pembelian'),
     path('jual/<int:id>/', views.penjualan, name='penjualan'),
     path('riwayat/', views.riwayat_barang, name='riwayat_barang'),



     ]