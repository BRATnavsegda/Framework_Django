from django.urls import path
from . import views

urlpatterns = [
    path('heads_or_tails/', views.heads_or_tails, name='heads_or_tails'),
    path('cube/', views.cube, name='cube'),
    path('rand_num/', views.rand_num, name='rand_num'),
]
