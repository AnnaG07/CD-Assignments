from django.urls import path
from . import views

urlpatterns = [
    path('', views.base),
    path('login', views.login),
    path('register', views.register),
    path('success', views.success),
    path('logout', views.logout_request),
]
