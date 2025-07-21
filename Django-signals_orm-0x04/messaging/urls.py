from django.urls import path
from . import views
from .views import delete_user

urlpatterns = [
    path('messages/<int:pk>/', views.message_detail, name='message_detail'),
    path("delete-account/", views.delete_user, name="delete_user"),
    path("account-deleted/", views.account_deleted, name="account_deleted"),
]
