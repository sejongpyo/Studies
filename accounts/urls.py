from django.conf.urls import url, include
from django.urls import path
from . import views

urlpatterns = [
    path('signin', views.signin, name="signin"),
    path('signin_insert', views.signin_insert, name="signin_insert"),
    path('login_form', views.login_form, name="login_form"),
    path('login', views.login, name="login"),
]