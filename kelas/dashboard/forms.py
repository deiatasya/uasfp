from django.forms import ModelForm
from dashboard.models import Barang, pakaian, kaoskaki
from django import forms

class FormBarang(ModelForm):
    class Meta:
        model=Barang
        fields='__all__'

        widgets = {
            'kodebrg': forms.TextInput({'class':'form-control'}),
            'nama': forms.TextInput({'class':'form-control'}),
            'stok': forms.NumberInput({'class':'form-control'}),
            'harga': forms.NumberInput({'class':'form-control'}),
            'link_gbr': forms.TextInput({'class':'form-control'}),
            'jenis_id': forms.Select({'class':'form-control'}),
        }

class Formpakaian(ModelForm):
    class Meta:
        model=pakaian
        fields='__all__'

        widgets = {
            'kodepakaian': forms.TextInput({'class':'form-control'}),
            'nama': forms.TextInput({'class':'form-control'}),
            'stok': forms.NumberInput({'class':'form-control'}),
            'harga': forms.NumberInput({'class':'form-control'}),
            'link_gbr': forms.TextInput({'class':'form-control'}),
            'jeniss_id': forms.Select({'class':'form-control'}),
        }
class Formkaoskaki(ModelForm):
    class Meta:
        model=kaoskaki
        fields='__all__'

        widgets = {
            'kodekaoskaki': forms.TextInput({'class':'form-control'}),
            'nama': forms.TextInput({'class':'form-control'}),
            'stok': forms.NumberInput({'class':'form-control'}),
            'harga': forms.NumberInput({'class':'form-control'}),
            'link_gbr': forms.TextInput({'class':'form-control'}),
            'jeniskk_id': forms.Select({'class':'form-control'}),
        }