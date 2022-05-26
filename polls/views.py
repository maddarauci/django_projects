from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import get_object_or_404, render
from django.urls import reverse
from django.views import generic

#from django.template import loader

from .models import Choice, Question

# Create your views here.


def IndexView(generic.ListView):
    template_name = 'polls/index.html'
    context_object_name = 'lastest_question_list'

    def get_queryset(self):
        """Return the last five published questions."""
        return Question.objects.order_by('-pub_date')[:5]


    #lastest_question_list = Question.objects.order_by('-pub_date')[:5]
    #context = {'lastest_question_list': lastest_question_list}
    #return render(request, 'polls/index.html', context)
    '''
    template = loader.get_template('polls/index.html')
    context = {
        'latest_question_list': lastest_question_list,
    }'''
    #return HttpResponse(template.render(context, request))
    #output = ', '.join([q.question_text for q in lastest_question_list])
    #return HttpResponse(output)
    #eturn HttpResponse("Hello, world. You're at the polls index.")



# might raise 404 error.
def DetailView(generic.DetailView):
    model = Question
    template_name = 'polls/detail.html'
    try:
        question = Question.objects.get(pk=question_id)
    except Question.DoesNotExist:
        raise Http404("Question does not exist")

    return render(request, 'polls/detail.html', {'question': question})
    #return HttpResponse("You are looking at question %s.", question_id)


def ResultsView(generic.DetailView):
    model = Question
    template_name = 'polls/results.html'
    question = get_object_or_404(Question, pk=question_id)
    return render(request, 'polls/results.html', {'question': question})
    response = "You are looking at the results of question %s."
    return HttpResponse(response % question_id)


def vote(request, question_id):
    question = get_object_or_404(Question, pk=question_id)
    try:
        selected_choice = question.choice_set.get(pk=request.POST['choice'])
    except (KeyError, Choice.DoesNotExist):
        # redisplay the question voting form.
        return render(request, 'polls/detail.html', {
            'question': question,
            'error_message': "You didn't select a choice"
        })
    else:
        selected_choice.votes += 1
        selected_choice.save()
        # Always return an HttpResonseRedirect after successfully dealing.
        # with POST data. This prevents data from being posted twice if a
        # user hits the back btn.
        return HttpResponseRedirect(reverse('polls:results', args=(question.id,)))
    #return HttpResponse("You are voting on question %s." % question_id)
