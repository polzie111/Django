from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader
from .models import Books


def my_book_web(request):
    books = Books.objects.order_by('Title')
    template = loader.get_template('index.html')
    context = {
        'books': books,
    }
    return HttpResponse(template.render(context, request))
def myNextPage(request):
    return HttpResponse("<b>To jest moja następna strona!</b>")

