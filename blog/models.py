from django.contrib.auth.models import User
from django.db import models
from ckeditor.fields import RichTextField
# Create your models here.
class Project(models.Model):
    name = models.CharField(max_length=200,verbose_name="Loyiha nomi",blank=False,null=False)
    author = models.ForeignKey(User,on_delete=models.CASCADE)
    image = models.ImageField(upload_to='project_images/')
    text = RichTextField(verbose_name='Loyiha haqida malumot')
    created_time = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name


class Blog(models.Model):
    name = models.CharField(max_length=200, verbose_name="blog nomi", blank=False, null=False)
    author = models.ForeignKey(User,on_delete=models.CASCADE)
    image = models.ImageField(upload_to='blog_images/')
    text = RichTextField(verbose_name='blog haqida malumot')
    created_time = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name

class Contact(models.Model):
    name = models.CharField(max_length=200, verbose_name="foydalanuvchi ismi", blank=False, null=False)
    email = models.EmailField(max_length=200,verbose_name='foydalanuvchi emaili')
    topic = models.CharField(max_length=100,verbose_name='mavzu')
    message = RichTextField(verbose_name='foydalanuvchi xabari')
    created_time = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name