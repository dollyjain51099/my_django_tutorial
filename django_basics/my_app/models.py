from django.db import models

# Create your models here.
class Posts(models.Model):
    Title = models.CharField(max_length=100)
    Posted_on = models.DateTimeField(auto_now_add=True, blank=True)
    Description = models.TextField(null=True)
    author = models.CharField(max_length=50)


