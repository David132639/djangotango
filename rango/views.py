from django.shortcuts import render

from django.http import HttpResponse
from rango.models import Category, Page

def index(request):
    #return HttpResponse("Rango says hey there partner!<br><a href=\"\\rango\\about\">About page</a>")
    #context_dicti = {'boldmessage': "Crunchy, creamy, cookie, candy, cupcake!"}
    category_list = Category.objects.order_by('-likes')[:5]
    context_dicti = {'categories': category_list}
    return render(request, 'rango/index.html', context=context_dicti)

def about(request):
    #return HttpResponse("Rango says here is the about page. <br><a href=\"\\\">Home page</a>")
    return render(request, 'rango/about.html')

def show_category(request, category_name_slug):
    context_dict = {}
    try:
        category = Category.objects.get(slug=category_name_slug)
        # Retrieve all of the associated pages.
        # Note that filter() will return a list of page objects or an empty list
        pages = Page.objects.filter(category=category)
        
        # Adds our results list to the template context under name pages.
        context_dict['pages'] = pages
        # We also add the category object from
        # the database to the context dictionary.
        # We'll use this in the template to verify that the category exists.
        context_dict['category'] = category
    except Category.DoesNotExist:
        context_dict['category'] = None
        context_dict['pages'] = None

    # Go render the response and return it to the client.
    return render(request, 'rango/category.html', context_dict)

