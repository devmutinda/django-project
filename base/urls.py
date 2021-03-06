from django.urls import path
from . import views

urlpatterns = [
    path('login/', views.loginPage, name="login"),
    path('topics/', views.topicsPage, name="topics"),
    path('register/', views.registerUser, name="register"),
    path('logout/', views.logoutUser, name="logout"),
    path('', views.home, name="home"),
    path('room-new/<str:pk>/', views.room, name="room"),
    path('create-form/', views.createRoom, name="form"),
    path('update-room/<str:pk>/', views.updateRoom, name="update"),
    path('delete-room/<str:pk>/', views.deleteRoom, name="delete"),
    path('delete-message/<str:pk>/', views.deleteMessage, name="delete-message"),
    path('user-profile/<str:pk>/', views.userProfile, name="profile"),
    path('update-profile/', views.updateUser, name="update-profile"),
    path('activity/', views.userActivity, name="activity")
]