# -*- coding: utf-8 -*-
from django.shortcuts import render
from app.models import Usuario,Articulo,VentaCompra,VentaCompraArticulos,Gastos,Insumos
from django.http import HttpResponse
from app.forms import ArticuloForm,GastosForm,InsumosForm
import datetime 
from django.db.models import Q
from django.db.models import Sum

def index(request):   
    return render(request,'index.html')

def login(request): 
    request.session.clear()
    request.session.flush()      
    return render(request,'login.html')

def validar(request):
    request.session.clear()
    request.session.flush()
    if request.POST: 
        #Guardar bitacora        
        try:            
            u=Usuario.objects.get(usuario=request.POST['usuario'])
            if u.contrasena == request.POST['contrasena']:
                if u.activo == False:
                    return HttpResponse(u'Usuario Inactivo')
                else:
                    request.session['nombre']=(u.nombre).title()
                    request.session['idusuario']=u.id  
                    request.session['tipousuario']=u.tipousuario.clave                                  
                    return HttpResponse('1')
            else:
                return HttpResponse(u'La contraseña no coincide')
        except Usuario.DoesNotExist:        
            return HttpResponse('El usuario no existe')
    return render(request,'login.html')    

def articulos(request):   
    articulos=Articulo.objects.all()                
    return render(request,'articulos/articulos.html',{'articulos':articulos})

def articulo_save(request):    
    if request.POST:
        id_=int(request.POST['id'])
        if id_ == 0:
            formulario = ArticuloForm(request.POST)
        else:
            articulo=Articulo.objects.get(pk=id_)
            formulario=ArticuloForm(request.POST,instance=articulo)                                
        if formulario.is_valid():            
            formulario.save() 
    return HttpResponse("")    

def articulo_delete(request,idarticulo):
    estado=0        
    try:  
        estado=1      
        Articulo.objects.get(pk=idarticulo).delete()
    except:
        estado=0
    return HttpResponse(estado)   

def articulo_frm(request):
    id_=0
    if request.GET:
        id_=request.GET['id']
        articulo=Articulo.objects.get(pk=id_)
        formulario=ArticuloForm(instance=articulo)
    else:    
        formulario=ArticuloForm()
    return render(request,'articulos/articulos_frm.html',{'formulario':formulario,'id':id_})   

def gastos(request):  
    if request.POST:        
        diaini,mesini,anioini=request.POST['fechaini'].split('/')
        diafin,mesfin,aniofin=request.POST['fechafin'].split('/')
        fechaini=datetime.datetime(int(anioini),int(mesini),int(diaini))
        fechafin=datetime.datetime(int(aniofin),int(mesfin),int(diafin))  
    else:    
        fechaini=datetime.datetime.now()
        fechafin=datetime.datetime.now()
    tiempoini=datetime.time.min
    tiempofin=datetime.time.max  
    fecha_inicial=datetime.datetime.combine(fechaini,tiempoini)
    fecha_final=datetime.datetime.combine(fechafin,tiempofin)           
    gastos=Gastos.objects.filter(Q(fecha__gte=fecha_inicial) & Q(fecha__lte=fecha_final))
    total=Gastos.objects.filter(Q(fecha__gte=fecha_inicial) & Q(fecha__lte=fecha_final)).aggregate(total=Sum('costo'))
    return render(request,'gastos/gastos.html',{'gastos':gastos,'total':total['total']})

def gastos_tbl(request):  
    if request.POST:        
        diaini,mesini,anioini=request.POST['fechaini'].split('/')
        diafin,mesfin,aniofin=request.POST['fechafin'].split('/')
        fechaini=datetime.datetime(int(anioini),int(mesini),int(diaini))
        fechafin=datetime.datetime(int(aniofin),int(mesfin),int(diafin))  
        tiempoini=datetime.time.min
        tiempofin=datetime.time.max  
        fecha_inicial=datetime.datetime.combine(fechaini,tiempoini)
        fecha_final=datetime.datetime.combine(fechafin,tiempofin)           
        gastos=Gastos.objects.filter(Q(fecha__gte=fecha_inicial) & Q(fecha__lte=fecha_final))
        total=Gastos.objects.filter(Q(fecha__gte=fecha_inicial) & Q(fecha__lte=fecha_final)).aggregate(total=Sum('costo'))
    return render(request,'gastos/gastos_tbl.html',{'gastos':gastos,'total':total['total']})

def gastos_save(request):    
    if request.POST:
        id_=int(request.POST['id'])
        if id_ == 0:
            formulario = GastosForm(request.POST)
        else:
            gastos=Gastos.objects.get(pk=id_)
            formulario=GastosForm(request.POST,instance=gastos)                                
        if formulario.is_valid():
            formulario.save() 
    return HttpResponse("")    

def gastos_frm(request):
    id_=0
    if request.GET:
        id_=request.GET['id']
        gastos=Gastos.objects.get(pk=id_)
        formulario=GastosForm(instance=gastos)
    else:    
        formulario=GastosForm()
    return render(request,'gastos/gastos_frm.html',{'formulario':formulario,'id':id_})   

def gastos_delete(request,idgasto):
    estado=0        
    try:  
        estado=1      
        Gastos.objects.get(pk=idgasto).delete()
    except:
        estado=0
    return HttpResponse(estado)   

def insumos(request):  
    if request.POST:        
        diaini,mesini,anioini=request.POST['fechaini'].split('/')
        diafin,mesfin,aniofin=request.POST['fechafin'].split('/')
        fechaini=datetime.datetime(int(anioini),int(mesini),int(diaini))
        fechafin=datetime.datetime(int(aniofin),int(mesfin),int(diafin))  
    else:    
        fechaini=datetime.datetime.now()
        fechafin=datetime.datetime.now()
    tiempoini=datetime.time.min
    tiempofin=datetime.time.max  
    fecha_inicial=datetime.datetime.combine(fechaini,tiempoini)
    fecha_final=datetime.datetime.combine(fechafin,tiempofin)           
    insumos=Insumos.objects.filter(Q(fecha__gte=fecha_inicial) & Q(fecha__lte=fecha_final))
    total=Insumos.objects.filter(Q(fecha__gte=fecha_inicial) & Q(fecha__lte=fecha_final)).aggregate(total=Sum('costo'))
    return render(request,'insumos/insumos.html',{'insumos':insumos,'total':total['total']})

def insumos_tbl(request):  
    if request.POST:        
        diaini,mesini,anioini=request.POST['fechaini'].split('/')
        diafin,mesfin,aniofin=request.POST['fechafin'].split('/')
        fechaini=datetime.datetime(int(anioini),int(mesini),int(diaini))
        fechafin=datetime.datetime(int(aniofin),int(mesfin),int(diafin))  
        tiempoini=datetime.time.min
        tiempofin=datetime.time.max  
        fecha_inicial=datetime.datetime.combine(fechaini,tiempoini)
        fecha_final=datetime.datetime.combine(fechafin,tiempofin)           
        insumos=Insumos.objects.filter(Q(fecha__gte=fecha_inicial) & Q(fecha__lte=fecha_final))
        total=Insumos.objects.filter(Q(fecha__gte=fecha_inicial) & Q(fecha__lte=fecha_final)).aggregate(total=Sum('costo'))
    return render(request,'insumos/insumos_tbl.html',{'insumos':insumos,'total':total['total']})

def insumos_save(request):    
    if request.POST:
        id_=int(request.POST['id'])
        if id_ == 0:
            formulario = InsumosForm(request.POST)
        else:
            insumos=Insumos.objects.get(pk=id_)
            formulario=InsumosForm(request.POST,instance=insumos)                                
        if formulario.is_valid():
            formulario.save() 
    return HttpResponse("")    

def insumos_frm(request):
    id_=0
    if request.GET:
        id_=request.GET['id']
        insumo=Insumos.objects.get(pk=id_)
        formulario=InsumosForm(instance=insumo)
    else:    
        formulario=InsumosForm()
    return render(request,'insumos/insumos_frm.html',{'formulario':formulario,'id':id_})   

def insumos_delete(request,idinsumo):
    estado=0        
    try:  
        estado=1      
        Insumos.objects.get(pk=idinsumo).delete()
    except:
        estado=0
    return HttpResponse(estado)  

def buscar_codigo(request,cantidad,codigo):
    try:
        articulo=Articulo.objects.get(codigo=codigo)
        subtotal=float(cantidad)*float(articulo.precioventa) 
        return render(request,'ventas/ventas_buscar.html',{'articulo':articulo,'cantidad':cantidad,'subtotal':subtotal})
    except Exception as e:
        print e 
    return render(request,'ventas/ventas_buscar.html')

def ventas(request):     
    return render(request,'ventas/ventas.html')

def ventas_save(request):
    idusuario=request.session['idusuario']
    u=Usuario.objects.get(pk=idusuario)  
    if request.POST:    
        if len(request.POST.getlist('codigo')) > 0:    
            venta=VentaCompra.objects.create(usuario=u,compraventa=True)
            for codigo in request.POST.getlist('codigo'):
                articulo=Articulo.objects.get(codigo=codigo)            
                try:
                    VentaCompraArticulos.objects.create(ventacompra=venta,articulo=articulo,cantidadinventario=1,iva=articulo.iva,preciocosto=articulo.preciocosto,precioventa=articulo.precioventa)
                    articulo.cantidadinventario=articulo.cantidadinventario-1
                    articulo.save()
                except Exception as e:
                    print e             
    return HttpResponse("")   

def buscar_codigo_compra(request,cantidad,codigo):
    try:        
        articulo=Articulo.objects.get(codigo=codigo)
        preciocosto=float(articulo.preciocosto)+(float(articulo.preciocosto)*(float(articulo.iva)*0.01))
        subtotal=float(cantidad)*preciocosto        
        return render(request,'compras/compras_buscar.html',{'articulo':articulo,'cantidad':cantidad,'subtotal':subtotal})
    except Exception as e:
        print e 
    return render(request,'compras/compras_buscar.html')

def compras(request):     
    return render(request,'compras/compras.html')

def compras_save(request):
    idusuario=request.session['idusuario']
    u=Usuario.objects.get(pk=idusuario)  
    if request.POST:    
        if len(request.POST.getlist('codigo')) > 0:                    
            compra=VentaCompra.objects.create(usuario=u,compraventa=False)
            for codigo in request.POST.getlist('codigo'):
                print codigo
                articulo=Articulo.objects.get(codigo=request.POST['articulo'+str(codigo)])
                print request.POST['cantidad'+str(codigo)]            
                try:                
                    cant=request.POST['cantidad'+str(codigo)]
                    VentaCompraArticulos.objects.create(ventacompra=compra,articulo=articulo,cantidadinventario=cant,iva=articulo.iva,preciocosto=articulo.preciocosto,precioventa=articulo.precioventa)
                    articulo.cantidadinventario=articulo.cantidadinventario+int(cant)
                    articulo.save()
                except Exception as e:
                    print e   
    return HttpResponse("")   

def reporte_ventas(request):
    return render(request,'reportes/reporte_ventas.html')

def reporte_ventas_tbl(request):    
    if request.POST:
        tiporeporte="Compras"
        tipo=request.POST['tipo']
        horaini,minini=request.POST['horaini'].split(':')
        horafin,minfin=request.POST['horafin'].split(':')
        diaini,mesini,anioini=request.POST['fechaini'].split('/')
        diafin,mesfin,aniofin=request.POST['fechafin'].split('/')
        fechaini=datetime.datetime(int(anioini),int(mesini),int(diaini))
        fechafin=datetime.datetime(int(aniofin),int(mesfin),int(diafin))
        #tiempoini=datetime.time.min
        #tiempofin=datetime.time.max    
        tiempoini=datetime.time(int(horaini),int(minini),0)
        tiempofin=datetime.time(int(horafin),int(minfin),0)
        fecha_inicial=datetime.datetime.combine(fechaini,tiempoini)
        fecha_final=datetime.datetime.combine(fechafin,tiempofin)
        compraventa=False
        if int(tipo)==1:
            compraventa=True
            tiporeporte="Ventas"
        ventas=VentaCompra.objects.filter(Q(fecha__gte=fecha_inicial) & Q(fecha__lte=fecha_final)).filter(compraventa=compraventa)
        vca=VentaCompraArticulos.objects.filter(ventacompra__in=ventas).values('articulo__id','articulo__precioventa','articulo__preciocosto','articulo__iva').annotate(total=Sum('cantidadinventario')).order_by('articulo__descripcion')
        print fecha_final
        items=[]
        ganancia=0
        monto=0
        costo=0
        cantidad=0
        for v in vca:
            articulo=Articulo.objects.get(pk=v['articulo__id'])
            item={}
            item['id']=v['articulo__id']
            item['total']=v['total']
            preciocosto=float(v['articulo__preciocosto'])+(float(v['articulo__preciocosto'])*(float(articulo.iva)*0.01))
            item['preciocosto']=preciocosto
            item['precioventa']=v['articulo__precioventa']
            item['descripcion']=articulo.descripcion
            item['codigo']=articulo.codigo
            item['monto']=float(articulo.precioventa)*float(v['total'])
            item['costo']=preciocosto*float(v['total'])
            item['diferencia']=float(item['monto'])-float(item['costo'])  
            ganancia+=float(item['diferencia']) 
            monto+=float(item['monto'])
            costo+=float(item['costo'])
            cantidad+=int(item['total'])      
            items.append(item)              
    return render(request,'reportes/reporte_ventas_tbl.html',{'ventas':items,'fechaini':fecha_inicial,'fechafin':fecha_final,'ganancia':ganancia,'monto':monto,'costo':costo,'cantidad':cantidad,'tiporeporte':tiporeporte})
