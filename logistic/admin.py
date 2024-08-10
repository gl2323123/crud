from django.contrib import admin

from logistic.models import Product, Stock, StockProduct


# Register your models here.

@admin.register(Product)
class SensorAdmin(admin.ModelAdmin):
    list_display = ['id', 'title', 'description']

@admin.register(Stock)
class StockAdmin(admin.ModelAdmin):
    pass

@admin.register(StockProduct)
class StockProductAdmin(admin.ModelAdmin):
    pass
