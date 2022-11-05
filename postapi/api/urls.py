from django.urls import path

from . import views

urlpatterns = [
    path('', views.getData, name='get_data'),
    path('add/', views.addItem, name='add_item'),
]
