from django.urls import path

from .views import AddClient, ClientPage, ProductView, UpdateProductView

urlpatterns = [
    path('client/add/', AddClient.as_view(), name='client_form'),
    path('client_page/<int:pk>/', ClientPage.as_view(), name='client_page'),
    path('product/<int:pk>/', ProductView.as_view(), name='product_page'),
    path('update_product/<int:pk>/', UpdateProductView.as_view(), name='update_product'),
]
