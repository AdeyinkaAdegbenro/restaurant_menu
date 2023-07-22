from django.db import models

# Create your models here.

class Menu(models.Model):
    name = models.CharField(max_length=30)
    when_created = models.DateTimeField(auto_now_add=True)
    when_updated = models.DateTimeField(auto_now=True)

class MenuItem(models.Model):
    name = models.CharField(max_length=30)
    menu = models.ForeignKey(Menu, on_delete=models.CASCADE)
    when_created = models.DateTimeField(auto_now_add=True)
    when_updated = models.DateTimeField(auto_now=True)