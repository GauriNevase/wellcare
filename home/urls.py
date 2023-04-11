from django.urls import path
from home import views
from blog import views as bv
from diary import views as dv
from chatbot import views as cv

urlpatterns = [
    path('', views.index, name="index"),
    path('community/', views.index2, name="community"),
    path('login/',views.login1 ,name="login"),
    path('afterlogin',views.afterlogin,name="afterlogin"),
    path('blog/', bv.PostList.as_view(), name='blog_home'),
    #path('<slug:slug>/', bv.PostDetail.as_view(), name='blog_post_detail'),
    path('diary/',dv.index,name='diary_home'),
    path('add/', dv.add,name='add'),
    path('chatbot/',cv.index,name='index'),
    path('getResponse',cv.getResponse,name='getResponse')
]
