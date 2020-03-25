from django.shortcuts import render, get_object_or_404
from .models import Question


# Create your views here.
def index(request):
    latest_question_list = Question.objects.order_by('-pub_date')[:5]
    # Provide the access of these variable to the template
    context: dict = {"latest_question_list": latest_question_list}
    # Give access to the template to variables in context and to the request object
    return render(request, "polls/index.html", context)


def detail(request, question_id):
    # try to get  Question.objects.get(pk=question_id) if the id doesn't match, return a 404
    question = get_object_or_404(Question, pk=question_id)
    context = {"question": question}
    return render(request, "polls/detail.html", context)


def results(request, question_id):
    # try to get  Question.objects.get(pk=question_id) if the id doesn't match, return a 404
    question = get_object_or_404(Question, pk=question_id)
    context = {"question": question}
    return render(request, "polls/results.html", context)


def vote(request, question_id):
    # try to get  Question.objects.get(pk=question_id) if the id doesn't match, return a 404
    question = get_object_or_404(Question, pk=question_id)
    context = {"question": question}
    return render(request, "polls/vote.html", context)
