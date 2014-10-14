#encoding:utf-8
from django import forms
from django.forms import Textarea
from app.models import Articulo,Gastos,Insumos,Proveedor,TipoInsumo,TipoGasto,TipoArticulo,MarcaArticulo

class ArticuloForm(forms.ModelForm):
    class Meta:
        model = Articulo
        widgets={
            "codigo":forms.TextInput(attrs={'required':'True'}),
            "descripcion":forms.TextInput(attrs={'required':'True'}),
            "tipoarticulo":forms.Select(attrs={'required':'True'}),
            "marcaarticulo":forms.Select(attrs={'required':'True'}),
            "unidadmedida":forms.Select(attrs={'required':'True'}),
            "iva":forms.TextInput(attrs={'required':'True','pattern':'^\d{0,2}?$'}),
            "preciocosto":forms.TextInput(attrs={'required':'True','pattern':'^\d+(\.\d{1,2})?$'}),
            "precioventa":forms.TextInput(attrs={'required':'True','pattern':'^\d+(\.\d{1,2})?$'}),
            "cantidadinventario":forms.TextInput(attrs={'required':'True','pattern':'^\d+$'}),
        }
    def __init__(self, *args, **kwargs):
        super(ArticuloForm, self).__init__(*args, **kwargs)
        self.fields['tipoarticulo'].empty_label = None        
        self.fields['tipoarticulo'].queryset = TipoArticulo.objects.order_by('descripcion')        
        self.fields['marcaarticulo'].empty_label = None        
        self.fields['marcaarticulo'].queryset = MarcaArticulo.objects.order_by('descripcion')        
        self.fields['unidadmedida'].empty_label = None   
    
    def clean_descripcion(self):
        return self.cleaned_data['descripcion'].upper()                          
        
class GastosForm(forms.ModelForm):
    class Meta:
        model = Gastos
        widgets={
            "tipogasto":forms.Select(attrs={'required':'True'}),
            "costo":forms.TextInput(attrs={'required':'True','pattern':'^\d+(\.\d{1,2})?$'}),
            "comentarios": Textarea(attrs={'cols': 80, 'rows': 4}),
        }        
    def __init__(self, *args, **kwargs):
        super(GastosForm, self).__init__(*args, **kwargs)
        self.fields['tipogasto'].empty_label = None        
        self.fields['tipogasto'].queryset = TipoGasto.objects.order_by('descripcion')        
   
        
class InsumosForm(forms.ModelForm):
    class Meta:
        model = Insumos
        widgets={
            "tipoinsumo":forms.Select(attrs={'required':'True'}),
            "proveedor":forms.Select(attrs={'required':'True'}),
            "unidadmedida":forms.Select(attrs={'required':'True'}),
            "cantidad":forms.TextInput(attrs={'required':'True','pattern':'^\d+$'}),
            "costo":forms.TextInput(attrs={'required':'True','pattern':'^\d+(\.\d{1,2})?$'}),            
        }        
        
    def __init__(self, *args, **kwargs):
        super(InsumosForm, self).__init__(*args, **kwargs)
        self.fields['proveedor'].empty_label = None        
        self.fields['proveedor'].queryset = Proveedor.objects.order_by('descripcion')        
        self.fields['tipoinsumo'].empty_label = None        
        self.fields['tipoinsumo'].queryset = TipoInsumo.objects.order_by('descripcion')