from django.contrib import admin
from . import models


@admin.action(description='Сбросить количество в ноль')
def reset_quantity(modeladmin, request, queryset):
    queryset.update(quantity=0)


@admin.register(models.Product)
class ProductAdmin(admin.ModelAdmin):
    """Список продуктов для админки"""
    list_display = ['name', 'category', 'quantity']
    ordering = ['category', '-quantity']
    list_filter = ['date_added', 'price']
    search_fields = ['description', 'name']
    search_help_text = 'Искать по названию и описанию'
    actions = [reset_quantity]

    """Отдельный продукт"""
    # fields = ['name', 'category', 'description', 'price', 'quantity', 'date_added', 'rating']
    readonly_fields = ['date_added', 'rating']
    fieldsets = [
        (
            None, {
                'classes': ['wide'],
                'fields': ['name'],
            }
        ),
        (
            'Описание', {
                'classes': ['collapse'],
                'description': 'Категория товара и его подробное описание',
                'fields': ['category', 'description'],
            }
        ),
        (
            'Цена и кол-во', {
                'fields': ['price', 'quantity'],
            }
        ),
        (
            'Рейтинг и прочее', {
                'description': 'Рейтинг сформирован автоматически',
                'fields': ['rating', 'date_added'],
            }
        )
    ]


# Register your models here.
# admin.site.register(models.Category)
# admin.site.register(models.Product, ProductAdmin)
