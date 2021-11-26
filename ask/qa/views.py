from django.core.paginator import Paginator, EmptyPage
from django.shortcuts import render, get_object_or_404
from .models import Question
# Create your views here.
from django.http import HttpResponse, Http404


def test(request, *args, **kwargs):
    return HttpResponse('OK')

def detail_question(request, pk):
    question = get_object_or_404(Question, pk=pk)
    context = {
        "question": question
        }
    return render(request, "qa/detail.html", context)

def paginate(request, qs):
    try:
        page_number = int(request.GET.get("page", 1))
    except ValueError:
        raise Http404
    paginator = Paginator(qs, 10)
    try:
        page_obj = paginator.get_page(page_number)
    except EmptyPage:
        page_obj = paginator.get_page(paginator.num_pages)
    return page_obj

def new_list(request):
    qs = Question.objects.new()
    page_obj = paginate(request, qs)
    context = {
        "page_obj": page_obj
    }
    return render(request, "qa/list.html", context)

def popular(request):
    qs = Question.objects.popular()
    page_obj = paginate(request, qs)
    context = {
        "page_obj": page_obj
    }
    return render(request, "qa/list.html", context)