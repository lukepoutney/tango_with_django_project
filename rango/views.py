from django.http import HttpResponse
from django.shortcuts import render
from rango.models import Category
from rango.models import Page

def index(request):
    category_list = Category.objects.order_by('-likes')[:5]
    page_list = Page.objects.order_by('-views')[:5]
    context_dict = {'categories': category_list,
                    'pages': page_list}

    # Return the rendered response and send it back!
    return render(request, 'rango/index.html', context_dict)

def about(request):
    return render(request, 'rango/about.html')

def show_category(request, category_name_slug):
    context_dict = {}

    try:
        category = Category.objects.get(slug=category_name_slug)

        # Retrieve all of the associated pages.
        pages = Page.objects.filter(category=category)

        # Adds our results list to the template context under name pages.
        context_dict['pages'] = pages

        context_dict['category'] = category
        
    except Category.DoesNotExist:
        
        # the template will display the "no category" message for us.
        context_dict['category'] = None
        context_dict['pages'] = None
        
    #Render the response and return it to the client.
    return render(request, 'rango/category.html', context_dict)
