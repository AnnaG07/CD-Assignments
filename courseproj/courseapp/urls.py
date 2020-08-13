from django.urls import path
from . import views

urlpatterns = [
    path('', views.base),
    #path('courses', views.courses),
    path('create', views.create),
    path('courses/destroy/<int:id>', views.destroy),
]