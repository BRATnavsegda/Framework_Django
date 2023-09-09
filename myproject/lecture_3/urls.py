from django.urls import path

from lecture_3.views import index, year_post, post_detail, MonthPost, TemplIf


urlpatterns = [
    path('', index, name='index'),
    path('posts/<int:year>/', year_post, name='year_post'),
    path('posts/<int:year>/<int:month>/', MonthPost.as_view(), name='month_post'),
    path('posts/<int:year>/<int:month>/<slug:slug>/', post_detail, name='post_detail'),
    path('if/', TemplIf.as_view(), name='templ_if'),
]
