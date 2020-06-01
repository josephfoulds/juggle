from django.shortcuts import render

from engine.models import Blog as BlogModel

from django.views.decorators.csrf import csrf_exempt
from django.utils.decorators import method_decorator

# Import views from API subfolder
from engine.api import blog, comment, post

# Index handling
def index(request):

    # GET / - Display all blogs
    # Retrieve all the blogs from the database and return them to the index template
    blogs = BlogModel.objects.all()
    context = {'blogs': blogs}
    return render(request, 'index.html', context=context)