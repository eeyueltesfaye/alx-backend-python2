from django.urls import path
from . import views

urlpatterns = [
    path('messages/<int:pk>/', views.message_detail, name='message_detail'),
]
