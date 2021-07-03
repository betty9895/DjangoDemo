from django.http import HttpResponse

def index(request):
    return HttpResponse('Helllo Django by HttpResponse')

