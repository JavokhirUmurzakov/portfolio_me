from django.shortcuts import render, redirect
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from .models import Project,Blog,Contact
from .forms import ContactForm
from django.core.mail import send_mail
from django.conf import settings

# Create your views here.
def home(request):
    projects = Project.objects.all()
    context = {
        'projects': projects,
    }
    return render(request,'index.html',context)

def blog(request,page=1):
    articles = Blog.objects.order_by('-id')
    paginator = Paginator(articles, 2)
    try:
        articles = paginator.page(page)
    except PageNotAnInteger:
        articles = paginator.page(1)
    except EmptyPage:
        articles = paginator.page(paginator.num_pages)

    context = {
        'objects': articles,
    }

    return render(request, 'blog.html', context)

def blog_detail(request,pk):
    blog_one = Blog.objects.get(id=pk)
    context = {
        'blog_one': blog_one,
    }
    return render(request,'blog01.html',context)

def about(request):
    return render(request,'about.html')

def work(request):
    projects = Project.objects.all()
    context = {
        'projects': projects,
    }
    return render(request,'work.html',context)

def work_detail(request,pk):
    project_one = Project.objects.get(id=pk)
    context = {
        'project_one': project_one,
    }
    return render(request,'work01.html',context)


def contact(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            name = form.cleaned_data['name']
            email = form.cleaned_data['email']
            topic = form.cleaned_data['topic']
            message = form.cleaned_data['message']

            contact = Contact.objects.create(name=name,email=email,topic=topic,message=message)
            contact.save()

            # Send an email

            return redirect('contact_page')
    else:
        form = ContactForm()

    return render(request, 'contact.html', {'form': form})