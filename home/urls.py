from django.urls import path
from home import views
from blog import views as cv


urlpatterns = [
    path('', views.index, name="index"),
    path('community/', views.index2, name="community"),
    path('login/',views.login ,name="login"),
    path('afterlogin/',views.afterlogin,name="aftelogin"),
    path('blog/', cv.PostList.as_view(), name='blog_home'),
    path('<slug:slug>/', cv.PostDetail.as_view(), name='blog_post_detail')
]
