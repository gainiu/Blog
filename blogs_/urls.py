'''定义blogs_的URL模式'''

from django.urls import path

from . import views

urlpatterns=[
    #主页
    path('',views.index,name='index'),

    #显示所有博文
    path('blogs/',views.blogs,name='blogs'),

    #显示特定博文详情
    path('blogs/<blogs_id>/',views.blog,name='blog'),

    #用于添加新博文的网页
    path('new_blog/',views.new_blog,name='new_blog'),

    #用于编辑博文的网页
    path('edit_blog/<blogs_id>/',views.edit_blog,name='edit_blog'),
]