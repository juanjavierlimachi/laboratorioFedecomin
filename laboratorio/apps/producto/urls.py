from django.conf.urls import patterns, include, url
from django.contrib import admin
from .views import *
urlpatterns = patterns('',
    
    url(r'^BuscarCliente/$', BuscarCliente),
    url(r'^BuscarCliente_view/$', BuscarCliente_view),
    
    url(r'^VerProductos/$', VerProductos),
    url(r'^RegistroProductoView/(?P<id>\d+)/$',RegistroProductoView),
    url(r'^kardex/(?P<id>\d+)/$',kardex),
    url(r'^NewClient/$', NewClient),
    url(r'^VerClientes/$', VerClientes),
    
    url(r'^NewElemento/$', NewElemento),
    url(r'^VerElementos/$', VerElementos),
    
    url(r'^por_cliente/(?P<id>\d+)/$',por_cliente),
    url(r'^buscarProducto_view/$', buscarProducto_view),
    url(r'^AgregarResultado/(?P<id>\d+)/$',AgregarResultado),
    url(r'^buscar/$',buscar),
    url(r'^crearReportes/$',CrearReportes),
    url(r'^outProduct/$',outProduct),
    url(r'^InprimirIngresoProductos/(?P<id>\d+)/(?P<inicio>[^/]+)/(?P<final>[^/]+)/$',InprimirIngresoProductos),

    url(r'^editCliente/(?P<id>\d+)/$',editCliente),
    url(r'^deleteCliente/(?P<id>\d+)/$',deleteCliente),
    url(r'^Delete_cliente/(?P<id>\d+)/$',Delete_cliente),
    url(r'^altaCliente/(?P<id>\d+)/$',altaCliente),
    url(r'^Alta_cliente/(?P<id>\d+)/$',Alta_cliente),
    url(r'^editProducto/(?P<id>\d+)/$',editProducto),
    url(r'^deleteProducto/(?P<id>\d+)/$',deleteProducto),
    url(r'^Delete_producto/(?P<id>\d+)/$',Delete_producto),
    url(r'^RecuperarProducto/(?P<id>\d+)/$',RecuperarProducto),
    url(r'^recuperar_producto/(?P<id>\d+)/$',recuperar_producto),
    url(r'^editResultado/(?P<id>\d+)/$',editResultado),
    url(r'^deleteResultado/(?P<id>\d+)/$',deleteResultado),
    url(r'^Delete_resultado/(?P<id>\d+)/$',Delete_resultado),

    url(r'^editElemento/(?P<id>\d+)/$',editElemento),
    
    url(r'^deleteElemento/(?P<id>\d+)/$',deleteElemento),
    url(r'^Delete_elemento/(?P<id>\d+)/$',Delete_elemento),
    url(r'^RecuperarElemento/(?P<id>\d+)/$',RecuperarElemento),
    
    url(r'^recuperar_elemento/(?P<id>\d+)/$',recuperar_elemento),
    url(r'^ImprimirRecibo/(?P<id>\d+)/$',ImprimirRecibo),
    url(r'^ImprimirCertificado/(?P<id>\d+)/(?P<copia>[^/]+)/$',ImprimirCertificado),
    url(r'^ImprimirDuplicado/(?P<id>\d+)/$',ImprimirDuplicado),
)
