from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name="home"),
    path('room_new/<str:pk>/', views.room, name="room"),
    path('create_form/', views.form, name="form"),
    path('update_room/<str:pk>/', views.updateRoom, name="update"),
    path('delete_room/<str:pk>/', views.deleteRoom, name="delete")
]