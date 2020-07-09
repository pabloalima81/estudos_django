from django.http import HttpResponse
from django.shortcuts import render

def do_calculation(value1, value2):
    return value1 + value2

def test_function(request):
    tot = do_calculation(20, 30)
    p_flag = False
    people = ['Maria', 'Pedro','Paulo', 'Jose']
    return render(request, 'example.html', {'total':tot, 'people': people, 'p_flag': p_flag})


def list_clients(request):
    return HttpResponse('Hello World')

def special_case_2003(request):
    return HttpResponse('Returning the cases for 2003')

def special_case(request, year):
    return HttpResponse('::Returning the cases for %s' % year)

def month_archive(request, year, month ):
    return HttpResponse('::Returning the cases for  year %s and month %s' % (year, month))

def hello(request, name):
    return HttpResponse('Hello %s' % name)