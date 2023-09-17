from django.urls import path
from . import views

urlpatterns = [
    path('index.html/',views.index,name='diary_home'),
    path('add/', views.add,name='add')
]
