from django.contrib import admin
from models import *

# Register your models here.


class ListShopAdmin(admin.ModelAdmin):
    list_display = ('id', 'idShopper', )


class DetailShopArticleAdmin(admin.ModelAdmin):
    list_display = ('id', 'idArticle', 'idListShop', 'quantity', 'subtotal' , 'state')

    def subTotal(self, obj):
    	cost = obj.calculateSbutotal()
    	return cost


   

    


admin.site.register(Shopper)
admin.site.register(ListShop, ListShopAdmin)
admin.site.register(Article)
admin.site.register(DetailShopArticle , DetailShopArticleAdmin)
