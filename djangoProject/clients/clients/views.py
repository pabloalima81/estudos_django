from django.http import HttpResponse

def list_clients(request):
    return HttpResponse('Hello World')