from django.shortcuts import render
from django.http import HttpResponse
from random import randint


def heads_or_tails(request):
    return HttpResponse('HEADS' if {randint(0, 1)} else 'TAILS')


def cube(request):
    return HttpResponse(str(randint(1, 6)))


def rand_num(request):
    return HttpResponse(str(randint(1, 100)))
