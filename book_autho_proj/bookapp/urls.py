from django.urls import path
from . import views

urlpatterns = [
    path('', views.base),
    path('books/create', views.create_book),
    path('books/<int:id>', views.view_book),
    path('books/<int:id>/assign', views.assign_book),
    path('books', views.books),
    path('authors/create', views.create_author),
    path('authors/<int:id>', views.view_author),
    path('authors/<int:id>/assign', views.assign_author),
    path('authors', views.authors),
]