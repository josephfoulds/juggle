from django.http import HttpResponse

from django.views import View

# Index handling
def index(request):
    return HttpResponse("Not yet implemented")

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