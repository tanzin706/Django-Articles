from datetime import date
from email.policy import default
from email.quoprimime import body_check
from sre_constants import SRE_FLAG_DEBUG
from django.db import models

class Article(models.Model):
    title = models.CharField(max_length=100)
    slug = models.SlugField()
    body = models.TextField()
    date = models.DateTimeField(auto_now_add=True)
    thumb = models.ImageField(default='default.png',blank=True)


    #add in author later
    #python manage.py makemigrations
    #python manage.py migrate
    #       {% %} used for python code like for loops
    #       {{ }} used for showing data only

    def __str__(self):
        return self.title

    def snippet(self):
        return self.body[:50]+'....'

