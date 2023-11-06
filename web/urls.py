from django.urls import path
from . import views

urlpatterns = [
    path("",views.index,name='index'),
    path("about",views.about,name='about'),
    path("blog",views.blog,name='blog'),
    path("blog-single",views.blogsingle,name='blog-single'),
    path("contact",views.contact,name='contact'),
    path("course",views.course,name='course'),
    path("main",views.main,name='main'),
    path("login",views.login1,name='login'),
    path("logout",views.logout_view,name='logout'),
]