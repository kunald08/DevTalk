from django.urls import path
from . import views


urlpatterns = [    
    path('', views.home, name="home"),
    path('index/', views.index),
    path('room_page/<str:pk>', views.room, name="room"),
]
