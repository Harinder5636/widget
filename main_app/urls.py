from django.urls import path
from . import views


urlpatterns = [
    path('', views.index, name="index"),
    path('add/', views.create_item, name='add_widget'),
    path('delete/<int:id>', views.delete, name='delete_item'),
]