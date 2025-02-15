from django.http import HttpResponse, Http404
from django.template import loader
from django.shortcuts import render
from .models import Question

# each function is a view. Each view is a model behavior mapped to the model's url interface. Standard Path -> Function.

def index(request):
    latest_questions_list = Question.objects.order_by("-pub_date")[:5]
    context = {"latest_questions_list": latest_questions_list}
    return render(request, "polls/index.html", context)

def detail(request, question_id):
    return HttpResponse(f"You're looking at question {question_id}")

def results(request, question_id):
    response = f"You're looking at the results of {question_id}"
    return HttpResponse(response)

def vote(request, question_id):
    return HttpResponse(f"You're voting on question {question_id}")