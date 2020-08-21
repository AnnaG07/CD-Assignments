from django.urls import path
from . import views

urlpatterns = [
    path('', views.books),
    path('add_book', views.add_book),
    path('delete/<int:id>', views.delete),
    path('view/<int:id>', views.view),
    path('favorite/<int:id>', views.favorite),
    path('unfavorite/<int:id>', views.unfavorite),
]