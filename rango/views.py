from django.shortcuts import render

from django.http import HttpResponse

def index(request):
    #return HttpResponse("Rango says hey there partner!<br><a href=\"\\rango\\about\">About page</a>")
    context_dicti = {'boldmessage': "Crunchy, creamy, cookie, candy, cupcake!"}
    return render(request, 'rango/index.html', context=context_dicti)

def about(request):
    #return HttpResponse("Rango says here is the about page. <br><a href=\"\\\">Home page</a>")
    return render(request, 'rango/about.html')
