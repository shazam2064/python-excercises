from django.db import models


# Create your models here
class ArticleModel(models.Model):
    tittle = models.CharField(max_length=100)
    category = models.CharField(max_length=100)
    author = models.CharField(max_length=100)
    content = models.TextField()
    created_at = models.DateTimeField()
