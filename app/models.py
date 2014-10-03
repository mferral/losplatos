#encoding:utf-8
from django.db import models
import datetime

class TipoUsuario(models.Model):
    clave=models.CharField(max_length=3)
    descripcion=models.CharField(max_length=30)
    def __unicode__(self):
        return self.clave
    
class UnidadMedida(models.Model):
    descripcion=models.CharField(max_length=30)
    def __unicode__(self):
        return self.descripcion

class TipoArticulo(models.Model):
    descripcion=models.CharField(max_length=30)
    def __unicode__(self):
        return self.descripcion

class MarcaArticulo(models.Model):
    descripcion=models.CharField(max_length=30)
    def __unicode__(self):
        return self.descripcion

class TipoAjusteInventario(models.Model):
    descripcion=models.CharField(max_length=30)
    def __unicode__(self):
        return self.descripcion

class Proveedor(models.Model):
    descripcion=models.CharField(max_length=30)
    def __unicode__(self):
        return self.descripcion

class TipoGasto(models.Model):
    descripcion=models.CharField(max_length=30)
    def __unicode__(self):
        return self.descripcion
    
class TipoInsumo(models.Model):
    descripcion=models.CharField(max_length=30)
    def __unicode__(self):
        return self.descripcion    

class Usuario(models.Model):
    nombre=models.CharField(max_length=100)
    usuario=models.CharField(max_length=50,unique=True)
    contrasena=models.CharField(max_length=18)
    activo=models.BooleanField(default=True)
    tipousuario=models.ForeignKey(TipoUsuario)       
    def __unicode__(self):
        return self.nombre
    
class Articulo(models.Model):
    codigo=models.CharField(max_length=50,unique=True)
    descripcion=models.CharField(max_length=200)
    iva=models.IntegerField()
    cantidadinventario=models.IntegerField(blank=True, null=True)
    preciocosto=models.DecimalField(max_digits=5, decimal_places=2)
    precioventa=models.DecimalField(max_digits=5, decimal_places=2)
    unidadmedida=models.ForeignKey(UnidadMedida)
    tipoarticulo=models.ForeignKey(TipoArticulo)
    marcaarticulo=models.ForeignKey(MarcaArticulo)
    def __unicode__(self):
        return self.descripcion      

class VentaCompra(models.Model):
    fecha=models.DateTimeField(default=datetime.datetime.now(),editable=False)        
    compraventa=models.BooleanField() # false=compra true=venta
    usuario=models.ForeignKey(Usuario)
    def __str__(self):
        return self.usuario.nombre
    
class VentaCompraArticulos(models.Model):
    cantidadinventario=models.IntegerField()
    iva=models.IntegerField()
    preciocosto=models.DecimalField(max_digits=5, decimal_places=2)
    precioventa=models.DecimalField(max_digits=5, decimal_places=2)
    articulo=models.ForeignKey(Articulo,on_delete=models.PROTECT)
    ventacompra=models.ForeignKey(VentaCompra)
    def __unicode__(self):
        return self.articulo.descripcion

    
class AjustesInventario(models.Model):
    fecha=models.DateTimeField(default=datetime.datetime.now(),editable=False)
    cantidadinventario=models.IntegerField()    
    entradasalida=models.BooleanField() # false=entrada true=salida
    tipoajusteinventario=models.ForeignKey(TipoAjusteInventario)
    articulo=models.ForeignKey(Articulo,on_delete=models.PROTECT)
    usuario=models.ForeignKey(Usuario)  
    def __unicode__(self):
        return self.articulo.descripcion    
    
class Gastos(models.Model):
    fecha=models.DateTimeField(default=datetime.datetime.now(),editable=False)
    comentarios=models.CharField(max_length=300,blank=True)
    costo=models.DecimalField(max_digits=5, decimal_places=2)
    tipogasto=models.ForeignKey(TipoGasto)
    usuario=models.ForeignKey(Usuario)
    def __unicode__(self):
        return self.tipogasto.descripcion

class Insumos(models.Model):
    fecha=models.DateTimeField(default=datetime.datetime.now(),editable=False)    
    costo=models.DecimalField(max_digits=5, decimal_places=2)
    tipoinsumo=models.ForeignKey(TipoInsumo)
    usuario=models.ForeignKey(Usuario)
    proveedor=models.ForeignKey(Proveedor)
    def __unicode__(self):
        return self.tipogasto.descripcion

