from django.contrib import admin
from .models import Project,Blog,Contact
# Register your models here.
@admin.register(Project)
class ProjectAdmin(admin.ModelAdmin):
    list_display = ['name','image','text','created_time']
    search_fields = ['name','text']

@admin.register(Blog)
class ProjectAdmin(admin.ModelAdmin):
    list_display = ['name','author','image','text','created_time']
    search_fields = ['name','text','author']

@admin.register(Contact)
class ProjectAdmin(admin.ModelAdmin):
    list_display = ['name','email','topic','message','created_time']
    search_fields = ['name','text','author']