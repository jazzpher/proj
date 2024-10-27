from django.urls import path
from .views.indexview import my_view

urlpatterns = [
    path('', my_view, name='index'),
]