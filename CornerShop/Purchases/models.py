from __future__ import unicode_literals

from django.db import models
from django.contrib.auth.models import User



class Shopper(models.Model):
	"""docstring for Shopper contiene datos de los compradores"""
	fristName = models.CharField(max_length=50)
	lastName = models.CharField(max_length=50)
	phone = models.CharField(max_length=13, help_text="+56911111111")
	usuario = models.OneToOneField(User)

	def __unicode__(self):
		return self.fristName

	



class ListShop(models.Model):
	"""docstring for ListShop contiene el la lista de listas de compra"""

	idShopper = models.ForeignKey(Shopper, blank=True, null=True)
	dateShop =  models.DateTimeField(auto_now_add=True)
	total = models.IntegerField(default= 0)

	def __unicode__(self):
		return "%s" % self.id 
		


class Article(models.Model):
	"""docstring for Article contiene  la informacion de los diferentes productos"""
	name = models.CharField(max_length=50)	
	unitCost = models.IntegerField(default=0)
	stock = models.IntegerField(default=0)
	def __unicode__(self):
		return self.name
		

# Create your models here.
class DetailShopArticle(models.Model):
	"""docstring for DetailShopArticle contiene el  detalle de cada articulo 
	a comprar, como  a que lista pertenese que producto es y la cantidad 
	a comprar y el subtotal de la compra del articulo """


	BOUGHT = '1'
	NO_BOUGHT = '2'
	INCOMPLETE = '3'

	STATE_SHOP_ARTICLE = (

		(BOUGHT, 'Comprado'),
		(NO_BOUGHT, 'No Comprado'),
		(INCOMPLETE, 'Compra Incompleta'),
		)

	idArticle = models.ForeignKey(Article)
	idListShop = models.ForeignKey(ListShop)
	quantity = models.IntegerField(default = 1)
	subtotal = models.IntegerField(default= 0)
	state =  models.CharField(max_length=20,choices=STATE_SHOP_ARTICLE)

	def __unicode__(self):
		return "%s" % self.idListShop.id

	def calculateSbutotal(self):
		a = self.idArticle.unitCost * self.quantity
		return a
	

	



	
from django.core.cache import cache
from django.db.models.signals import post_save
from django.dispatch import receiver

from django.contrib.sessions.models import Session

@receiver(post_save)
def clear_cache(sender, **kwargs):
    if sender != Session:
        cache.clear()

	