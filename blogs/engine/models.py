from django.db import models

class Blog(models.Model):
    name = models.CharField(max_length=200)

class Post(models.Model):
    blog = models.ForeignKey(Blog, on_delete=models.CASCADE)
    content = models.CharField(max_length=1000)
    name = models.CharField(max_length=200)

class Comment(models.Model):
    post = models.ForeignKey(Post, on_delete=models.CASCADE)
    content = models.CharField(max_length=200)
    author = models.CharField(max_length=50)
