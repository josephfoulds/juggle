from django.http import HttpResponse
from django.shortcuts import render
from django.views import View

from engine.models import Blog as BlogModel
from engine.models import Post as PostModel
from engine.models import Comment as CommentModel

from django.views.decorators.csrf import csrf_exempt
from django.utils.decorators import method_decorator

# View for handling comment resources
class Comment(View):
    # POST /blog/[BLOG_ID]/post/[POST_ID]/comment - Create new comment
    def post(self, request, blog_id=None, post_id=None, comment_id=None):
        content = request.POST.get("content", "")
        author  = request.POST.get("author", "")

        # Validation functions for POST data, fail with an HTTP400
        if not blog_id or not post_id or not content or not author or comment_id:
            return HttpResponse(status=400)

        # Error handling for server errors
        try:
            # Identify the blog from passed in blog ID
            b = BlogModel.objects.get(id=blog_id)

            # Identify the post from the passed in post ID
            p = PostModel.objects.get(id=post_id, blog=b)

            # Create a new comment and save it
            p = CommentModel(post=p, content=content, author=author)
            p.save()

        except Exception as e:
            # Return HTTP500 on server error
            return HttpResponse(status=500)

        # Return HTTP200
        return(HttpResponse())

    # DELETE /blog/[BLOG_ID]/post/[POST_ID]/comment/[COMMENT_ID] - Delete comment
    def delete(self, request, blog_id=None, post_id=None, comment_id=None):
        # Validation functions for DELETE, fail with an HTTP400
        if not blog_id or not post_id or not comment_id:
            return HttpResponse(status=400)

        # Error handling for server errors
        try:
            # Identify the blog from passed in blog ID
            b = BlogModel.objects.get(id=blog_id)

            # Identify the blog from passed in post ID
            p = PostModel.objects.get(id=post_id, blog=b)

            # Identify the comment from the passed in comment ID
            c = CommentModel.objects.get(id=comment_id, post=p)

            # Delete the comment
            c.delete()

        except Exception as e:
            # Return HTTP500 on server error
            return HttpResponse(status=500)

        # Return HTTP200
        return(HttpResponse())

    # Exempt requests from inbuilt CSRF detection, neccessary for rapid MVP API testing
    # nb: This should not be integrated in production unless security procedures are added to mitigate CSRF vulnerabilities
    @method_decorator(csrf_exempt)
    def dispatch(self, request, *args, **kwargs):
        return super(Comment, self).dispatch(request, *args, **kwargs)