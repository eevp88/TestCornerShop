from django.shortcuts import render_to_response,get_object_or_404, render
from django.http import HttpResponse,HttpResponseRedirect
from models import *

# Create your views here.
from django.views.generic import ListView, DetailView




class LispShopListview(ListView):
	""" docstring for LispShopListview  vista que muestra las listas de Compras disponibles """

	model = ListShop
	template_name = 'list_shop.html'


def listShopDetail(request,id_listshop):
	"""docstring for listShopDetail vista que carga el detalle de la lista"""
	ls = ListShop.objects.all()
	cat = get_object_or_404(ListShop, id = id_listshop)

	lista = DetailShopArticle.objects.filter(idListShop = cat)
	for obj in lista:
		obj.subtotal = obj.quantity * obj.idArticle.unitCost
		obj.save()
	template = "listShop_detail.html"
	return render(request, template,{"lista" : lista , "request":request })