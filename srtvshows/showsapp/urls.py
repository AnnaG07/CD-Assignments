from django.urls import path
from . import views

urlpatterns = [
    path('', views.base),
    path('shows/<int:id>', views.view_show),
    path('shows/edit/<int:id>', views.edit),
    path('shows/update/<int:id>', views.update),
    path('shows/delete/<int:id>', views.delete),
    path('shows/new', views.new),
    path('shows/create', views.create),
]