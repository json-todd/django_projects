from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader
from .models import Question

def index(request):
    latest_question_list = Question.objects.order_by('-pub_date')[:5]
    output = ','.join([q.question_text for q in latest_question_list])
    template = loader.get_template('polls/index.html')
    context = {
        'latest_question_list': latest_question_list,
    }
    return render(request, 'polls/index.html', context)

def results(request, question_id):
    return HttpResponse(f"You're looking at the results of question {question_id}.")

def detail(request, question_id):
    return HttpResponse(f"You're looking at question {question_id}")

def vote(request, question_id):
    return HttpResponse(f"You're voting on question {question_id}")

def owner(request):
    return HttpResponse("Hello, world. 223c4a00 is the polls index")
