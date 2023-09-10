from datetime import datetime

from django.shortcuts import render
from django.views.generic import DetailView, ArchiveIndexView, YearArchiveView, MonthArchiveView, WeekArchiveView

from myproject.hw_3 import models



class CustomerView(DetailView):
    model = models.Client
    template_name = 'hw_3/customer_page.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['current_date'] = datetime.now()
        return context


class AllProducts(ArchiveIndexView):
    model = models.Order
    date_field = 'ordered_at'
    template_name = 'hw_3/orders.html'
    allow_future = False
    week_format = '%U'
    year_format = '%Y'

    def get_context_data(self, **kwargs):
        customer = models.Client.objects.get(pk=self.kwargs.get('pk'))
        orders = super().get_queryset().filter(customer=customer).prefetch_related('products')
        products = set(product for order in orders for product in order.products.values_list('title'))

        context = super().get_context_data(**kwargs)
        context['products'] = products
        context['customer'] = customer

        return context

    def get_queryset(self, **kwargs):
        orders = models.Order.objects.get_queryset().filter(customer=self.kwargs.get('pk'))

        return orders


class AllYearProducts(AllProducts, YearArchiveView):
    pass


class AllMonthProducts(AllProducts, MonthArchiveView):
    pass


class AllWeekProducts(AllProducts, WeekArchiveView):
    pass


# Create your views here.

# class OrdersView(DetailView):
#     model = Order
#     template_name = 'hw_3/orders.html'
#     context_object_name = 'order'
#
#     def get_context_data(self, **kwargs):
#         context = super().get_context_data(**kwargs)
#         context['title'] = 'Заказы'
#         context['orders'] = Order.objects.all()
#
#         return context
