from django.conf.urls import patterns, include, url

from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    url(r'^$', 'app.views.index', name='principal'),
    url(r'^login/', 'app.views.login', name='login'),
    url(r'^validar/', 'app.views.validar'),

    url(r'^inventario/', 'app.views.articulos'),
    url(r'^articulo_frm/$', 'app.views.articulo_frm'),
    url(r'^articulo_save/', 'app.views.articulo_save'),
    url(r'^articulo_delete/(?P<idarticulo>\d+)','app.views.articulo_delete'),
    
    url(r'^gastos/', 'app.views.gastos'),
    url(r'^gastos_frm/$', 'app.views.gastos_frm'),
    url(r'^gastos_save/', 'app.views.gastos_save'),
    url(r'^gastos_tbl/', 'app.views.gastos_tbl'),
    url(r'^gastos_delete/(?P<idgasto>\d+)','app.views.gastos_delete'),
    
    url(r'^insumos/', 'app.views.insumos'),
    url(r'^insumos_frm/$', 'app.views.insumos_frm'),
    url(r'^insumos_save/', 'app.views.insumos_save'),
    url(r'^insumos_tbl/', 'app.views.insumos_tbl'),
    url(r'^insumos_delete/(?P<idinsumo>\d+)','app.views.insumos_delete'),    
        
    url(r'^ventas/', 'app.views.ventas'),
    url(r'^ventas_save/', 'app.views.ventas_save'),
    url(r'^buscar_codigo/(?P<codigo>.*)$', 'app.views.buscar_codigo'),
        
    url(r'^compras/', 'app.views.compras'),
    url(r'^compras_save/', 'app.views.compras_save'),
    url(r'^buscar_codigo_compra/(?P<cantidad>\d+)/(?P<codigo>.*)$', 'app.views.buscar_codigo_compra'),
        
    url(r'^reporte_ventas/', 'app.views.reporte_ventas'),
    url(r'^reporte_ventas_tbl/', 'app.views.reporte_ventas_tbl'),
        
    url(r'^admin/', include(admin.site.urls)),
)
