from django.http import HttpResponse
from django.shortcuts import render
from django.views import View

from engine.models import Blog as BlogModel
from engine.models import Post as PostModel
from engine.models import Comment as CommentModel

from django.views.decorators.csrf import csrf_exempt
from django.utils.decorators import method_decorator

# View for handling post resources
class Post(View):

    # GET /blog/[BLOG_ID]/post/[POST_ID] - Show post data + comments
    def get(self, request, blog_id=None, post_id=None):
        if not blog_id or not post_id:
            return HttpResponse(status=404)

        # Identify the post and blog from passed in post ID / blog ID
        try:
            b = BlogModel.objects.get(id=blog_id)
            p = PostModel.objects.get(id=post_id, blog=b)
        except Exception as e:
            # Return HTTP500 on server error
            return HttpResponse(status=404)

        # Identify any comments associated with the post
        try:
            c = CommentModel.objects.filter(post = p)
        except Exception as e:
            # Return HTTP500 on server error
            return HttpResponse(status=500)

        # Return the templated post and context
        context = {'post': p, 'comments':c, 'blog':b}
        return render(request, 'post.html', context=context)

    # POST /blog/[BLOG_ID]/post/ - Create new post
    def post(self, request, blog_id=None, post_id=None):
        content = request.POST.get("content", "")
        name    = request.POST.get("name", "")

        # Validation functions for POST data, fail with an HTTP400
        if not name or not content or post_id:
            return HttpResponse(status=400)

        # Error handling for server errors
        try:
            # Identify the blog from passed in blog ID
            b = BlogModel.objects.get(id=blog_id)

            # Create a new post and save it
            p = PostModel(blog=b, content=content, name=name)
            p.save()

        except Exception as e:
            # Return HTTP500 on server error
            return HttpResponse(status=500)

        # Return HTTP200
        return(HttpResponse())

    # DELETE /blog/[BLOG_ID]/post/[POST_ID] - Delete post
    def delete(self, request, blog_id=None, post_id=None):
        # Validation functions for DELETE, fail with an HTTP400
        if not blog_id or not post_id:
            return HttpResponse(status=400)

        # Error handling for server errors
        try:
            # Identify the blog from passed in blog ID
            b = BlogModel.objects.get(id=blog_id)

            # Identify the post from passed in post ID
            p = PostModel.objects.get(id=post_id, blog=b)

            # Delete the post
            p.delete()

        except Exception as e:
            # Return HTTP500 on server error
            return HttpResponse(status=500)

        # Return HTTP200
        return(HttpResponse())

    # Exempt requests from inbuilt CSRF detection, neccessary for rapid MVP API testing
    # nb: This should not be integrated in production unless security procedures are added to mitigate CSRF vulnerabilities
    @method_decorator(csrf_exempt)
    def dispatch(self, request, *args, **kwargs):
        return super(Post, self).dispatch(request, *args, **kwargs)