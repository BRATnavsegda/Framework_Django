
import logging
from django.shortcuts import render
from django.http import HttpResponse

logger = logging.getLogger(__name__)


def index(request):
    logger.info("index page log")
    return HttpResponse("Главная страница.")


def about(request):
    logger.info("index page log")
    return HttpResponse("Страница обо мне.")


# Create your views here.
