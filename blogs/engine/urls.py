from django.urls import path

from . import views

urlpatterns = [
    ### Engine Resources
    # GET / - Display all blogs
    path('', views.index, name='index'),

    ### Blog Resources
    # POST /blog/ - Create new blog
    # GET /blog/[BLOG_ID]/ - Show all posts on blog
    # DELETE /blog/[BLOG_ID]/ - Delete blog
    path('blog/', views.Blog.as_view()),
    path('blog/<int:blog_id>/', views.Blog.as_view()),

    ### Post Resources
    # POST /blog/[BLOG_ID]/post/ - Create new post
    # GET /blog/[BLOG_ID]/post/[POST_ID] - Show post data + comments
    # DELETE /blog/[BLOG_ID]/post/[POST_ID] - Delete post
    path('blog/<int:blog_id>/post/', views.Post.as_view()),
    path('blog/<int:blog_id>/post/<int:post_id>/', views.Post.as_view()),

    ### Comment Resources
    # POST /blog/[BLOG_ID]/post/[POST_ID]/comment - Create new comment
    # DELETE /blog/[BLOG_ID]/post/[POST_ID]/comment/[COMMENT_ID] - Delete comment
    path('blog/<int:blog_id>/post/<int:post_id>/comment/', views.Comment.as_view()),
    path('blog/<int:blog_id>/post/<int:post_id>/comment/<int:comment_id>/', views.Comment.as_view()),
]
