from django.shortcuts import render
from django.http import HttpResponseRedirect,Http404
from django.urls import reverse
from django.contrib.auth.decorators import login_required
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
    context={'blog':blog}
    return render(request,'blogs_/blog.html',context)

@login_required
def new_blog(request):
    '''添加新博文'''
    if request.method!='POST':
        form=BlogForm()
    else:
        form=BlogForm(request.POST)
        if form.is_valid():
            new_blog=form.save(commit=False)
            new_blog.owner=request.user
            new_blog.save()
            return HttpResponseRedirect(reverse('blogs_:blogs'))
    context={'form':form}
    return render(request,'blogs_/new_blog.html',context)

@login_required
def edit_blog(request,blogs_id):
    '''编辑博文'''
    blog=BlogPost.objects.get(id=blogs_id)
    check_blog_owner(blog,request)
    if request.method!='POST':
        form=BlogForm(instance=blog)
    else:
        form=BlogForm(instance=blog,data=request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse('blogs_:blog',args=[blog.id]))
    context={'blog':blog,'form':form}
    return render(request,'blogs_/edit_blog.html',context)

def check_blog_owner(blog,request):
    if blog.owner!=request.user:
        raise Http404