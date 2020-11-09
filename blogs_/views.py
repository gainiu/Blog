from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.urls import reverse
from .models import BlogPost
from .forms import BlogForm

# Create your views here.
def index(request):
    '''Blog主页'''
    return render(request,'blogs_/index.html')

def blogs(request):
    '''博文列表'''
    blogs=BlogPost.objects.order_by('date_added')
    context={'blogs':blogs}
    return render(request,'blogs_/blogs.html',context)

def blog(request,blogs_id):
    '''博文详情'''
    blog=BlogPost.objects.get(id=blogs_id)
    context={'blog_title':blog.title,'content':blog.text,'date_added':blog.date_added,'blog_id':blog.id}
    return render(request,'blogs_/blog.html',context)

def new_blog(request):
    '''添加新博文'''
    if request.method!='POST':
        form=BlogForm()
    else:
        form=BlogForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse('blogs_:blogs'))
    context={'form':form}
    return render(request,'blogs_/new_blog.html',context)

def edit_blog(request,blogs_id):
    '''编辑博文'''
    blog=BlogPost.objects.get(id=blogs_id)
    if request.method!='POST':
        form=BlogForm(instance=blog)
    else:
        form=BlogForm(instance=blog,data=request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse('blogs_:blog',args=[blog.id]))
    context={'blog':blog,'form':form}
    return render(request,'blogs_/edit_blog.html',context)