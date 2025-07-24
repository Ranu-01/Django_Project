from django import forms
from .models import Barang,Pembelian

class StockForm(forms.ModelForm):
    class Meta:
        model = Barang
        fields = ['nama_barang', 'quantity']


class PembelianForm(forms.ModelForm):
    class Meta:
        model = Pembelian
        fields = ['jumlah']

    def clean_jumlah(self):
        jumlah = self.cleaned_data['jumlah']
        if jumlah < 1:
            raise forms.ValidationError("Jumlah minimal pembelian adalah 1.")
        return jumlah
    
class PenjualanForm(forms.Form):
    jumlah = forms.IntegerField(min_value=1, label='Jumlah Penjualan')

    