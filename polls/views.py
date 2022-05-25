from ctypes.wintypes import HPALETTE
from curses.ascii import HT
from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.

'''
def index(request):
    return HttpResponse("Hello, world. You're at the polls index.")

'''

def detail(request, question_id):
    return HttpResponse("You are looking at question %s.", question_id)


def resluts(request, question_id):
    response = "You are looking at the results of question %s."
    return HttpResponse(response % question_id)


def vote(request, question_id):
    return HttpResponse("You are voting on question %s." % question_id)
    