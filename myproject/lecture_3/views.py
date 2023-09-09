from django.shortcuts import render
from django.http import JsonResponse, HttpResponse
from django.views import View
from django.views.generic import TemplateView


# Create your views here.
#
# return JsonResponse(post, json_dumps_params={'ensure_ascii': False})


def index(request):
    context = {
        'title': 'Главная страница'
    }
    return render(request, 'lecture_3/index.html', context)


def post_detail(request, year, month, slug):
    ...  # Формируем статьи за год и месяц по идентификатору. Пока обойдёмся без запросов к базе данных
    post = {
        "year": year,
        "month": month,
        "slug": slug,
        "title": "Кто быстрее создаёт списки в Python, list() или[]",
        "content": "В процессе написания очередной программы задумался над тем, какой способ создания списков в Python "
                   "работает быстрее... "
    }
    return JsonResponse(post, json_dumps_params={'ensure_ascii': False})


def year_post(request, year):
    text = ""
    ...  # формируем статьи за год
    return HttpResponse(f"Posts from {year}<br>{text}")


class MonthPost(View):

    def get(self, request, year, month):
        text = ""
        ...  # формируем статьи за год и месяц
        return HttpResponse(f"Posts from {month}/{year}<br>{text}")


class TemplIf(TemplateView):
    template_name = "lecture_3/templ_if.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['message'] = "Привет, мир!"
        context['number'] = 5
        return context

