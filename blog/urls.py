from django.urls import path
from .views import home,blog,work,about,contact,work_detail,blog_detail
urlpatterns = [
    path('',home,name='home_page'),
    path('about/',about,name='about_page'),
    path('projects/',work,name='work_page'),
    path('project/<int:pk>/',work_detail,name='work_detail_page'),
    path('blogs/<int:page>/',blog,name='blogs_page'),
    path('blog/<int:pk>/',blog_detail,name='blog_page'),
    path('contact/',contact,name='contact_page'),
]