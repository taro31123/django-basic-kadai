from django.contrib import admin
from.models import Product, Category

class ProductAdmin(admin.ModelAdmin):
     list_display = ('id', 'name', 'price', 'category')
     search_fields = ('name',)
     # ('',)にしないとタプル形式として認識されない
     list_filter = ('category',)

class CategoryAdmin(admin.ModelAdmin):
     list_display = ('id', 'name')
     search_fields = ('name',)

admin.site.register(Product, ProductAdmin)
admin.site.register(Category, CategoryAdmin)
