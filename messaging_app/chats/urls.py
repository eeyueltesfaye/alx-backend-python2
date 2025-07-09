from django.urls import path, include 
from .views import UserViewSet,ConversationViewSet, MessageViewSet
from rest_framework import routers 
from rest_framework.routers import DefaultRouter
from rest_framework_nested.routers import NestedDefaultRouter



router = routers.DefaultRouter()
router.register(r'users', UserViewSet)
router.register(r'conversations', ConversationViewSet)

conversation_router = NestedDefaultRouter(router, r'conversations', lookup='conversation')
conversation_router.register(r'messages', MessageViewSet, basename='conversation-messages')

conversation_router.register(r'participants', UserViewSet, basename='conversation-participants')


urlpatterns = [
    path('', include(router.urls)),
    path('', include(conversation_router.urls)),
]
