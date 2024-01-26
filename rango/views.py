from django.shortcuts import render
from django.http import HttpResponse

def index(request):
    #return HttpResponse("<a href='/rango/about/'>About</a>")
    context_dict = {'boldmessage': 'Crunchy, creamy, cookie, candy, cupcake!'} # Construct a dictionary to pass to the template engine as its context.
    return render(request, 'rango/index.html', context=context_dict)


def about(request):
    return HttpResponse(" <a href='/rango/'>Index</a>")
    #context_dict = {}
    #response = render(request, 'rango/about.html', context_dict)
    #return response



