from django.urls import path
from . import views

urlpatterns = [
    path('login/', views.loginPage, name="login"),
    path('register/', views.registerUser, name="register"),
    path('logout/', views.logoutUser, name="logout"),
    path('', views.home, name="home"),
    path('room-new/<str:pk>/', views.room, name="room"),
    path('create-form/', views.createRoom, name="form"),
    path('update-room/<str:pk>/', views.updateRoom, name="update"),
    path('delete-room/<str:pk>/', views.deleteRoom, name="delete")
]