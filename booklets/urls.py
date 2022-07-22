from django.urls import path
from django.contrib.auth import views as authViews

from . import views

urlpatterns=[
path('',views.index,name='index'),
path('login/',authViews.LoginView.as_view(template_name='login.html'),name='login'),
path('logout/',authViews.LogoutView.as_view(template_name='logout.html'),name='logout'),
path('register/',views.register),
path('upload/',views.addBooklet)
]
