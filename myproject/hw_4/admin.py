from django.contrib import admin

from . import models


# Register your models here.
@admin.register(models.Client)
class ClientAdmin(admin.ModelAdmin):

    """Список клиентов"""
    list_display = ['name', 'email', 'phone', 'address', 'date_reg']
    ordering = ['name', 'date_reg']
    search_fields = ['name', 'email']
    search_help_text = 'Искать по имени или электронной почте'

    """Отдельный клиент"""
    readonly_fields = ['date_reg']
    fieldsets = [
        (
            None, {
                'classes': ['wide'],
                'fields': ['name', 'date_reg'],

            }
        ),
        (
            'Контактные данные', {
                'classes': ['wide'],
                'fields': ['email', 'phone', 'address'],
            }
        ),
        (
            'Список заказов', {
                'classes': ['wide'],
                'fields': ['orders'],
            }
        )
    ]


@admin.register(models.Product)
class ProductAdmin(admin.ModelAdmin):

    """Список продуктов"""
    list_display = ['name', 'price', 'quantity']
    ordering = ['name', 'price', '-quantity']
    search_fields = ['description', 'name']
    search_help_text = 'Искать по названию или описанию'

    """Отдельный продукт"""
    readonly_fields = ['date_add']
    fieldsets = [
        (
            None, {
                'classes': ['wide'],
                'fields': ['image', 'name'],
            }
        ),
        (
            'Описание', {
                'classes': ['wide'],
                'description': 'Подробное описание товара',
                'fields': ['description', 'date_add'],
            }
        ),
        (
            'Цена и кол-во', {
                'fields': ['price', 'quantity'],
            }
        ),
    ]


@admin.register(models.Order)
class OrderAdmin(admin.ModelAdmin):

    """Список заказов"""
    list_display = ['customer', 'total_price', 'date_order']
    ordering = ['customer', 'date_order', '-total_price']
    search_fields = ['customer']
    search_help_text = 'Искать по клиенту'

    """Отдельный заказ"""
    readonly_fields = ['date_order']
    fieldsets = [
        (
            None, {
                'classes': ['wide'],
                'fields': ['customer'],
            }
        ),
        (
            'Список товаров', {
                'classes': ['wide'],
                'fields': ['products', 'total_price'],
            }
        ),
        (
            'Дата заказа', {
                'classes': ['wide'],
                'fields': ['date_order'],
            }
        )
    ]



