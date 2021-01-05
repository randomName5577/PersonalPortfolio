from django.db import models


# Create your models here.
class ContactMe(models.Model):
    name = models.CharField(max_length=30)
    email = models.EmailField()
    body = models.TextField()
    created_on = models.DateTimeField(auto_now_add=True)
    replied_to = models.BooleanField(default=False)

    def __str__(self):
        return self.name
