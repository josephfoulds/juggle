from django.http import HttpResponse
from django.shortcuts import render
from django.views import View

from engine.models import Blog as BlogModel

# Index handling
def index(request):
    # Retrieve all the blogs from the database and return them to the index template
    blogs = BlogModel.objects.all()
    context = {'blogs': blogs}
    return render(request, 'index.html', context=context)

# View for handling blog resources
class Blog(View):

    def get(self, request, blog_id=None):
        return HttpResponse("Not yet implemented")

# View for handling post resources
class Post(View):

    def get(self, request, blog_id=None, post_id=None):
        return HttpResponse("Not yet implemented")

# View for handling comment resources
class Comment(View):

    def get(self, request, blog_id=None, post_id=None, comment_id=None):
        return HttpResponse("Not yet implemented")