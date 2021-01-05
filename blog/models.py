from django.db import models
import django.dispatch
from django.conf import settings
from ckeditor.fields import RichTextField

# Create your models here.
class Category(models.Model):
    name = models.CharField(max_length=20)

    def __str__(self):
        return self.name

class Post(models.Model):
    title = models.CharField(max_length=255)
    #body = models.TextField()
    body = RichTextField(blank=True,null=True)
    created_on = models.DateTimeField(auto_now_add=True)
    last_modified = models.DateTimeField(auto_now=True)
    categories = models.ManyToManyField('Category', related_name='posts')
    abs_image = models.FilePathField(path='/home/homepc/PycharmProjects/djangoProject/blog/static/images')

    @property
    def get_photo_url(self):
        return self.abs_image.split('static')[1]

    def __str__(self):
        return self.title

# @django.dispatch.receiver(models.signals.post_init, sender = Post)
# def set_default_post_image_location:
#     if not instance.

class Comment(models.Model):
    author = models.CharField(max_length=60)
    body = models.TextField()
    email = models.EmailField()
    created_on = models.DateTimeField(auto_now_add=True)
    post = models.ForeignKey('Post', on_delete=models.CASCADE)

    def __str__(self):
        return self.author

