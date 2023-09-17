from django.urls import path
from home import views 
from blog import views as bv
from diary import views as dv
from chatbot import views as cv
from django.urls import path, re_path
# from chartapp import views as ccv



urlpatterns = [
    # Your existing URL patterns
    path('', views.index, name="index"),
    path('comm.html/', views.index2, name="community"),
    re_path(r'^comm\.html/ac\.html/$', views.ac, name="ac"),
    re_path(r'^comm\.html/dc\.html/$', views.dc, name="dc"),  # Updated pattern
    re_path(r'^comm\.html/ms\.html/$', views.ms, name="ms"),  # Updated pattern
    re_path(r'^comm\.html/aissues\.html/$', views.anger, name="aissues"),  # Updated pattern
    re_path(r'^comm\.html/Hi\.html/$', views.Hi, name="Hi"),  # Updated pattern
    re_path(r'^comm\.html/ri\.html/$', views.ri, name="ri"),  # Updated pattern
    path('login.html/', views.login1, name="login"),
    path('afterlogin', views.afterlogin, name="afterlogin"),
    path('diary.html/', dv.index, name='diary_home'),
    path('add/', dv.add, name='add'),  # Moved the 'add' pattern here
    path('blog/', bv.PostList.as_view(), name='blog_home'),
    path('<slug:slug>/', bv.PostDetail.as_view(), name='blog_post_detail'),
    # path('diary.html/', dv.index, name='diary_home'),
    # path('add/', dv.add, name='add/'),  # Moved the 'add' pattern here
    path('chatbot/', cv.index, name='index'),
    path('getResponse', cv.getResponse, name='getResponse')
]
