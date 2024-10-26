from django.urls import path
from shop.views.indexview import my_view

urlpatterns = [
    path('', my_view, name="my_view"),
]