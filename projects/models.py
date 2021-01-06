from django.db import models
from ckeditor.fields import RichTextField

# Create your models here.

class Technology(models.Model):
    name = models.CharField(max_length=20)

    def __str__(self):
        return self.name


class Project(models.Model):
    title = models.CharField(max_length=100)
    body = RichTextField(blank=True, null=True)
    technology = models.ManyToManyField('Technology',related_name='categories')
    image = models.FilePathField(path="/home/jaysonturk/PersonalPortfolio/projects/static/images")
    #image = models.FilePathField(path='/home/homepc/PycharmProjects/djangoProject/projects/static/images')
    github_link = models.CharField(max_length=255,blank=True)

    def __str__(self):
        return self.title

    @property
    def get_photo_url(self):
        return self.image.split('static')[1]


