#encoding:utf-8
from django.shortcuts import render, render_to_response
from .models import *
from laboratorio.apps.producto.models import *
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse, HttpResponseRedirect
from django.template import RequestContext
from django.contrib.auth.forms import User
from django.db.models import Q
from .forms import *
import datetime
import calendar
from datetime import datetime, date, time, timedelta
import StringIO
from xhtml2pdf import pisa
from django.template.loader import render_to_string
# Create your views here.
def BuscarCliente(request):

	return render(request,"producto/BuscarCliente.html")

def RegistroProductoView(request,id):
	#Usuario=Producto(Usuario=request.user)
	if request.method=='POST':
		#cliente=Cliente(Cliente=int(id))
		producto=Producto()
		producto.Nro_de_Lote=request.POST['Nro_de_Lote'].upper()
		producto.Precio=float(request.POST['Precio'])
		producto.Total=float(request.POST['Cantidad'])*float(request.POST['Precio'])
		producto.Observaciones=request.POST['Observaciones']
		producto.Cliente_id=int(id)
		producto.Elemento_id=int(request.POST['Elemento'])
		producto.Procedencia=request.POST['Procedencia'].upper()
		producto.Ficha=request.POST['Ficha']
		producto.Usuario_id=int(request.user.id)
		producto.save()
		return HttpResponse("ok")
	else:
		forms=FormProducto()
	return render(request,"producto/RegistroProductoView.html",{'ids':id,'forms':forms})
def VerProductos(request):
	fecha=datetime.now()
	final="%s-%s-%s" % (fecha.year,fecha.month,fecha.day)#fecha actual del sistema
	print "la fecha",fecha
	inicio="%s-%s-01" % (fecha.year,fecha.month)
	productos=Producto.objects.filter(fecha_registro__range=(inicio,fecha)).order_by("-id")
	clientes=Cliente.objects.filter(estado=True).order_by("-id")
	cant=Producto.objects.filter(fecha_registro__range=(inicio,fecha)).count()
	dic={
		'productos':productos,
		'clientes':clientes,
		'cant':cant
		}
	return render(request,"producto/VerProductos.html",dic)

def BuscarCliente_view(request):
	if request.method=="POST":
		texto=request.POST["cliente"]
		busqueda=(
			Q(Nombre__icontains=texto) |
			Q(Apellidos__icontains=texto) |
			Q(Ci_Nit__icontains=texto)
		)
		resultados=Cliente.objects.filter(busqueda).distinct()
		print "Clente:",resultados
		return render_to_response('producto/buscar.html',{'resultados':resultados},context_instance=RequestContext(request))
	else:
		texto=request.GET["cliente"]
		busqueda=(
			Q(Nombre__icontains=texto) |
			Q(Apellidos__icontains=texto) |
			Q(Ci_Nit__icontains=texto)
		)
		resultados=Cliente.objects.filter(busqueda).distinct()
		return render_to_response('producto/buscar.html',{'resultados':resultados},context_instance=RequestContext(request))

def kardex(request, id):
	producto=Producto.objects.get(id=int(id))
	resultados=Resultado.objects.filter(producto_id=int(id))
	print resultados
	dic={
		'producto':producto,
		'resultados':resultados
	}
	return render(request,'producto/kardex.html',dic)
def NewClient(request):
	if request.method=='POST':
		forms=FormCliente(request.POST)
		if forms.is_valid():
			forms.save()
			cod=Cliente.objects.latest('id')
			cod=cod.id
			print "ultimos; ",cod
			return HttpResponse(cod)
	else:
		forms=FormCliente()

	return render(request,'producto/NewClient.html',{'forms':forms})
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
def VerClientes(request):
	datos=Cliente.objects.all().order_by('-id')
	cliente=Cliente.objects.all().count()

	paginator=Paginator(datos,20)
	page = request.GET.get('page')
	try:
		contenido = paginator.page(page)
	except PageNotAnInteger:
		contenido = paginator.page(1)
	except EmptyPage:
		contenido = paginator.page(paginator.num_pages)
	return render(request,'producto/VerClientes.html',{'cliente':cliente,'contenido':contenido,'datos':contenido})

def NewElemento(request):
	if request.method=='POST':
		forms=FormElemento(request.POST)
		if forms.is_valid():
			forms.save()
			return HttpResponse("ok")
	else:
		forms=FormElemento()
	return render(request,'producto/NewElemento.html',{'forms':forms})

def VerElementos(request):
	datos=Elemento.objects.all().order_by('-id')
	cliente=Elemento.objects.filter(estado=True).count()
	return render(request,'producto/VerElementos.html',{'datos':datos,'cliente':cliente})

def por_cliente(request, id):
	productos=Producto.objects.filter(Cliente_id=int(id)).order_by("-id")
	cant=Producto.objects.filter(estado=True,Cliente_id=int(id)).count()
	dic={
		'productos':productos,
		'cant':cant
		}
	return render(request,"producto/por_cliente.html",dic)

def buscarProducto_view(request):
	if request.method=="POST":
		texto = request.POST['p']
		busqueda=(
				Q(Nro_de_Lote__icontains=texto) |
				Q(id__icontains=texto) |
				Q(id__icontains=texto)
			)
		productos=Producto.objects.filter(busqueda).distinct()
		return render_to_response('producto/buscarProducto_view.html',{'productos':productos},context_instance=RequestContext(request))
	else:
		texto=request.GET['p']
		print texto
		busqueda=(
				Q(Nro_de_Lote__icontains=texto) |
				Q(id__icontains=texto) |
				Q(id__icontains=texto)
			)
		productos=Producto.objects.filter(busqueda).distinct()
		return render_to_response('producto/buscarProducto_view.html',{'productos':productos},context_instance=RequestContext(request))

def AgregarResultado(request,id):
	if request.method=='POST':
		resp = Resultado()
		resp.Resultado =float(request.POST['Resultado'])
		resp.Elemento=request.POST['Elemento']
		resp.Abreviatura=request.POST['Abreviatura']
		resp.producto_id = int(id)
		resp.save()
		return HttpResponse("ok")
	else:
		forms=FormResultado()
	return render(request,'producto/AgregarResultado.html',{'forms':forms,'id':id})
def generar_pdf(html):
	resultado=StringIO.StringIO()
	pdf=pisa.pisaDocument(StringIO.StringIO(html.encode("UTF:8")),resultado)
	if not pdf.err:
		return HttpResponse(resultado.getvalue(),'application/pdf')
	return HttpResponse("Error al generar el reporte")
def ImprimirCertificado(request,id):
	producto=Producto.objects.get(id=int(id))
	resultados=Resultado.objects.filter(producto_id=int(id))
	print resultados
	fecha=datetime.now()
	fe="%s/%s/%s" % (fecha.day,fecha.month,fecha.year)
	dic={
		'producto':producto,
		'resultados':resultados,
		'fe':fe
	}
	html=render_to_string('producto/ImprimirCertificado.html',dic,context_instance=RequestContext(request))
	return generar_pdf(html)
	#return render(request,'producto/ImprimirCertificado.html',dic,context_instance=RequestContext(request))

def buscar(request):
    if request.method=="POST":
        #"""Aqui ira otra busqueda igual que abajo"""
        #return HttpResponse("hecho")
        texto=request.POST["q"]
        busqueda=(
            Q(Nombre__icontains=texto) |
            Q(Apellidos__icontains=texto) |
            Q(Ci_Nit__icontains=texto)
        )
        resultados=Cliente.objects.filter(busqueda).distinct()
        print "Clente:",resultados
        return render_to_response('producto/FormbuscarCliente.html',{'resultados':resultados},context_instance=RequestContext(request))

    else:
        texto=request.GET["q"]
        busqueda=(
            Q(Nombre__icontains=texto) |
            Q(Apellidos__icontains=texto) |
            Q(Ci_Nit__icontains=texto)
        )
        resultados=Cliente.objects.filter(busqueda).distinct()
        return render_to_response('producto/FormbuscarCliente.html',{'resultados':resultados},context_instance=RequestContext(request))

def CrearReportes(request):
	fecha=datetime.now()
	final="%s-%s-%s" % (fecha.year,fecha.month,fecha.day)#fecha actual del sistema
	print "la fecha",fecha
	inicio="%s-%s-01" % (fecha.year,fecha.month)
	productos=Producto.objects.filter(fecha_registro__range=(inicio,fecha),estado=True).order_by("-id")
	clientes=Cliente.objects.filter(estado=True).order_by("-id")
	cant=Producto.objects.filter(fecha_registro__range=(inicio,fecha),estado=True).count()
	dic={
		'productos':productos,
		'clientes':clientes,
		'cant':cant
		}
	return render(request,"producto/CrearReportes.html",dic)

def outProduct(request):
	if request.method=='POST':
		fecha=datetime.now()
		fe="%s-%s-%s" % (fecha.day,fecha.month,fecha.year)#fecha actual del sistema

		inicio=datetime.strptime(request.POST['inicio'],"%d/%m/%Y")
		print "inicio",inicio
		final=datetime.strptime(request.POST['final'],"%d/%m/%Y")
		print "final",final
		if str(inicio) > str(final):
			return HttpResponse("Error La Fecha Inicio No pueder ser Mayor a la Fecha Final.")
		final = final + timedelta(days=1)
		user=int(request.POST['user'])
		print "el usuario",user
		if user != 0:
			t_productos=Producto.objects.filter(Cliente_id=user,fecha_registro__range=(inicio,final),estado=True).count()
			productos=Producto.objects.filter(Cliente_id=user,fecha_registro__range=(inicio,final),estado=True)
			cliente = Cliente.objects.get(id=user)
			total = 0
			client = Cliente.objects.get(id=user)
			for i in productos:
				total = total + i.Total
			dat={
				'productos':productos,
				't_productos':t_productos,
				'cliente':cliente,
				'total':total,
				'client':client,
				'inicio':inicio.date(),
				'final':final.date() - timedelta(days=1)
			}
			return render_to_response('producto/outProduct.html',dat,context_instance=RequestContext(request))
		else:
			t_productos=Producto.objects.filter(fecha_registro__range=(inicio,final),estado=True).count()
			productos=Producto.objects.filter(fecha_registro__range=(inicio,final),estado=True)

			total = 0
			for i in productos:
				total = total + i.Total
			dat={
				'productos':productos,
				't_productos':t_productos,
				'total':total,
				'inicio':inicio.date(),
				'final':final.date() - timedelta(days=1)
			}
			return render_to_response('producto/outProduct.html',dat,context_instance=RequestContext(request))

def InprimirIngresoProductos(request, id,inicio, final):
	inicio=inicio
	inicio=datetime.strptime(inicio,"%d-%m-%Y")
	final=final
	final=datetime.strptime(final,"%d-%m-%Y")
	if request.method=='GET':
		fecha=datetime.now()
		if str(inicio) > str(final):
			return HttpResponse("Error La Fecha Inicio No pueder ser Mayor a la Fecha Final.")
		final = final + timedelta(days=1)
		if int(id) != 0:
			t_productos=Producto.objects.filter(Cliente_id=id,fecha_registro__range=(inicio,final),estado=True).count()
			productos=Producto.objects.filter(Cliente_id=id,fecha_registro__range=(inicio,final),estado=True)
			cliente = Cliente.objects.get(id=id)
			total = 0
			client = Cliente.objects.get(id=id)
			for i in productos:
				total = total + i.Total
			dat={
				'pagesize':'A4',
				'productos':productos,
				't_productos':t_productos,
				'cliente':cliente,
				'total':total,
				'client':client,
				'inicio':inicio.date(),
				'final':final.date() - timedelta(days=1),
				'fecha':fecha.date()
			}
			html=render_to_string('producto/InprimirIngresoProductos.html',dat,context_instance=RequestContext(request))
			return generar_pdf(html)
		else:
			t_productos=Producto.objects.filter(fecha_registro__range=(inicio,final),estado=True).count()
			productos=Producto.objects.filter(fecha_registro__range=(inicio,final),estado=True)

			total = 0
			for i in productos:
				total = total + i.Total
			dat={
				'pagesize':'A4',
				'productos':productos,
				't_productos':t_productos,
				'total':total,
				'inicio':inicio.date(),
				'final':final.date() - timedelta(days=1),
				'fecha':fecha.date()
			}
			html=render_to_string('producto/InprimirIngresoProductos.html',dat,context_instance=RequestContext(request))
			return generar_pdf(html)

def editCliente(request, id):
	dato=Cliente.objects.get(id=int(id))
	if request.method=='POST':
		forms=FormCliente(request.POST,instance=dato)
		if forms.is_valid():
			forms.save()
			return HttpResponse("La información se actualizó correctamente.")
	else:
		forms=FormCliente(instance=dato)
	return render(request,'producto/editCliente.html',{'forms':forms,'ids':id})
def deleteCliente(request,id):
	dato=Cliente.objects.get(id=int(id))
	return render(request,'crud/deleteCliente.html',{'dato':dato},context_instance=RequestContext(request))
def Delete_cliente(request,id):
	Cliente.objects.filter(id=int(id)).update(estado=False)
	return HttpResponse("La información se dió de baja correctamente.")
def altaCliente(request, id):
	dato=Cliente.objects.get(id=int(id))
	return render(request,'crud/altaCliente.html',{'dato':dato},context_instance=RequestContext(request))
def Alta_cliente(request,id):
	Cliente.objects.filter(id=int(id)).update(estado=True)
	return HttpResponse("La información se dió de alta correctamente.")

def editProducto(request,id):
	dato=Producto.objects.get(id=int(id))
	if request.method=='POST':
		forms=FormProducto(request.POST,instance=dato)
		if forms.is_valid():
			forms.save()
			return HttpResponse("La información se actualizó correctamente.")
	else:
		forms=FormProducto(instance=dato)
	return render(request,'crud/editProducto.html',{'forms':forms,'ids':id})

def deleteProducto(request,id):
	dato=Producto.objects.get(id=int(id))
	return render(request,'crud/deleteProducto.html',{'dato':dato},context_instance=RequestContext(request))
def Delete_producto(request,id):
	Producto.objects.filter(id=int(id)).update(estado=False)
	return HttpResponse("La información se dió de baja correctamente.")
def RecuperarProducto(request,id):
	dato=Producto.objects.get(id=int(id))
	return render(request,'crud/RecuperarProducto.html',{'dato':dato},context_instance=RequestContext(request))
def recuperar_producto(request,id):
	Producto.objects.filter(id=int(id)).update(estado=True)
	return HttpResponse("La información se dió de alta correctamente.")
def editResultado(request,id):
	dato=Resultado.objects.get(id=int(id))
	if request.method=='POST':
		forms=FormResultado(request.POST,instance=dato)
		if forms.is_valid():
			forms.save()
			return HttpResponse("La información se actualizó correctamente.")
	else:
		forms=FormResultado(instance=dato)
	return render(request,'crud/editResultado.html',{'forms':forms,'ids':id,'dato':dato})

def deleteResultado(request,id):
	dato=Resultado.objects.get(id=int(id))
	return render(request,'crud/deleteResultado.html',{'dato':dato},context_instance=RequestContext(request))
def Delete_resultado(request,id):
	dato=Resultado.objects.get(id=int(id))
	dato.delete()
	return HttpResponse("La información se dió de baja correctamente.")

def editElemento(request,id):
	dato=Elemento.objects.get(id=int(id))
	if request.method=='POST':
		forms=FormElemento(request.POST,instance=dato)
		if forms.is_valid():
			forms.save()
			return HttpResponse("La información se actualizó correctamente.")
	else:
		forms=FormElemento(instance=dato)
	return render(request,'crud/editElemento.html',{'forms':forms,'ids':id})
def deleteElemento(request,id):
	dato=Elemento.objects.get(id=int(id))
	return render(request,'crud/deleteElemento.html',{'dato':dato},context_instance=RequestContext(request))
def Delete_elemento(request, id):
	Elemento.objects.filter(id=int(id)).update(estado=False)
	return HttpResponse("La información se dió de baja correctamente.")

def RecuperarElemento(request, id):
	dato=Elemento.objects.get(id=int(id))
	return render(request,'crud/RecuperarElemento.html',{'dato':dato},context_instance=RequestContext(request))	
def recuperar_elemento(request, id):
	Elemento.objects.filter(id=int(id)).update(estado=True)
	return HttpResponse("La información se dió de alta correctamente.")

def ImprimirRecibo(request, id):
	producto=Producto.objects.get(id=int(id))
	fecha=datetime.now().date()
	valores=['UNO','DOS','TRES','CUATRO','CINCO','SEIS','SIETE','OCHO','NUEVE','DIEZ','VEINTE', 'TRENTA','CUARENTA','CINCUENTA']
	
	dic={
		'pagesize':'A4',
		'producto':producto,
		'fecha':fecha
	}
	html = render_to_string('crud/ImprimirRecibo.html',dic)	
	return generar_pdf(html)
def ImprimirDuplicado(request, id):
	producto=Producto.objects.get(id=int(id))
	resultados=Resultado.objects.filter(producto_id=int(id))
	print resultados
	fecha=datetime.now()
	fe="%s-%s-%s" % (fecha.day,fecha.month,fecha.year)
	dic={
		'producto':producto,
		'resultados':resultados,
		'fe':fe
	}
	html=render_to_string('crud/ImprimirDuplicado.html',dic,context_instance=RequestContext(request))
	return generar_pdf(html)


