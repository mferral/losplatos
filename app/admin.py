'''
Created on 22/09/2014

@author: miguelangelferral
'''
from django.contrib import admin
from app.models import Usuario,TipoUsuario,UnidadMedida,TipoArticulo,MarcaArticulo,TipoAjusteInventario,TipoGasto,Proveedor,TipoInsumo

# Register your models here.
admin.site.register(Usuario)
admin.site.register(TipoUsuario)
admin.site.register(UnidadMedida)
admin.site.register(TipoArticulo)
admin.site.register(MarcaArticulo)
admin.site.register(TipoAjusteInventario)
admin.site.register(TipoGasto)
admin.site.register(Proveedor)
admin.site.register(TipoInsumo)
