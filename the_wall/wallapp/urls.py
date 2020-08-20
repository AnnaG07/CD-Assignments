from django.urls import path
from . import views

urlpatterns = [
    path('', views.wall),
    path('post_message', views.post_message),
    path('delete_message/<int:id>', views.delete_message),
    path('edit_message/<int:id>', views.edit_message),
    path('update_message/<int:id>', views.update_message),
    path('post_comment/<int:id>', views.post_comment),
    path('delete_comment/<int:id>', views.delete_comment),
    path('edit_comment/<int:id>', views.edit_comment),
    path('update_comment/<int:id>', views.update_comment),
]