#from ctypes.wintypes import HPALETTE
#from curses.ascii import HT
from django.http import HttpResponse
from django.shortcuts import render
from django.template import loader

from . models import Question

# Create your views here.


def index(request):
    lastest_question_list = Question.objects.order_by('-pub_date')[:5]
    context = {'lastest_question_list': lastest_question_list}
    return render(request, 'polls/index.html', context)
    '''
    template = loader.get_template('polls/index.html')
    context = {
        'latest_question_list': lastest_question_list,
    }'''
    #return HttpResponse(template.render(context, request))
    #output = ', '.join([q.question_text for q in lastest_question_list])
    #return HttpResponse(output)
    #eturn HttpResponse("Hello, world. You're at the polls index.")



def detail(request, question_id):
    return HttpResponse("You are looking at question %s.", question_id)


def results(request, question_id):
    response = "You are looking at the results of question %s."
    return HttpResponse(response % question_id)


def vote(request, question_id):
    return HttpResponse("You are voting on question %s." % question_id)
