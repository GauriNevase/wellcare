from django.urls import path
from home import views 
from blog import views as bv
from diary import views as dv
from chatbot import views as cv
from django.urls import path, re_path

urlpatterns = [
    # Your existing URL patterns
    path('', views.index, name="index"),
    path('comm.html/', views.index2, name="community"),
    re_path(r'^comm\.html/ac\.html/$', views.ac, name="ac"),
    re_path(r'^comm\.html/dc\.html/$', views.dc, name="dc"),  
    re_path(r'^comm\.html/ms\.html/$', views.ms, name="ms"),  
    re_path(r'^comm\.html/aissues\.html/$', views.anger, name="aissues"),  
    re_path(r'^comm\.html/Hi\.html/$', views.Hi, name="Hi"), 
    re_path(r'^comm\.html/ri\.html/$', views.ri, name="ri"), 
    path('login.html/', views.login1, name="login"),
    path('afterlogin', views.afterlogin, name="afterlogin"),
    path('diary.html/', dv.index, name='diary_home'),
    path('add/', dv.add, name='add'),  
    path('blog/', bv.PostList.as_view(), name='blog_home'),
    path('<slug:slug>/', bv.PostDetail.as_view(), name='blog_post_detail'),
    path('chatbot/', cv.index, name='index'),
    path('getResponse', cv.getResponse, name='getResponse')
]
