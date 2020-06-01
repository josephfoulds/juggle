from django.http import HttpResponse
from django.shortcuts import render
from django.views import View

from engine.models import Blog as BlogModel
from engine.models import Post as PostModel

from django.views.decorators.csrf import csrf_exempt
from django.utils.decorators import method_decorator

# Index handling
def index(request):
    # GET / - Display all blogs

    # Retrieve all the blogs from the database and return them to the index template
    blogs = BlogModel.objects.all()
    context = {'blogs': blogs}
    return render(request, 'index.html', context=context)

# View for handling blog resources
class Blog(View):

    # GET /blog/[BLOG_ID]/ - Show all posts on blog
    def get(self, request, blog_id=None):
        if not blog_id:
            return HttpResponse(status=404)

        # Identify the blog from passed in blog ID
        try:
            b = BlogModel.objects.get(id=blog_id)
        except Exception as e:
            # Return HTTP404 on missing blog
            return HttpResponse(status=404)

        p = PostModel.objects.filter(blog_id = b)

        context = {'posts': p, 'blog': b}
        return render(request, 'blog.html', context=context)

    # POST /blog/ - Create new blog
    def post(self, request, blog_id=None):
        name = request.POST.get("name", "")

        # Validation functions for POST data, fail with an HTTP400
        if not name or blog_id:
            return HttpResponse(status=400)

        # Error handling for server errors
        try:
            # Create a new blog and save it
            b = BlogModel(name=name)
            b.save()
        except Exception as e:
            # Return HTTP500 on server error
            return HttpResponse(status=500)

        # Return HTTP200
        return(HttpResponse())

    # DELETE /blog/[BLOG_ID]/ - Delete blog
    def delete(self, request, blog_id=None):
        # Validation functions for DELETE, fail with an HTTP400
        if not blog_id:
            return HttpResponse(status=400)

        # Error handling for server errors
        try:
            # Identify the blog from passed in blog ID
            b = BlogModel.objects.get(id=blog_id)

            # Create a new blog and delete it
            b.delete()

        except Exception as e:
            # Return HTTP500 on server error
            return HttpResponse(status=500)

        # Return HTTP200
        return(HttpResponse())

    # Exempt requests from inbuilt CSRF detection, neccessary for rapid MVP API testing
    # nb: This should not be integrated in production unless security procedures are added to mitigate CSRF vulnerabilities
    @method_decorator(csrf_exempt)
    def dispatch(self, request, *args, **kwargs):
        return super(Blog, self).dispatch(request, *args, **kwargs)

# View for handling post resources
class Post(View):

    def get(self, request, blog_id=None, post_id=None):
        return HttpResponse("Not yet implemented")

# View for handling comment resources
class Comment(View):

    def get(self, request, blog_id=None, post_id=None, comment_id=None):
        return HttpResponse("Not yet implemented")