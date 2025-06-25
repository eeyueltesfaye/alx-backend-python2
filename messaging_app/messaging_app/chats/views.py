from django.shortcuts import render
from .serializers import UserSerializer, MessageSerializer, ConversationSerializer
from .models import User, Message, Conversation
from rest_framework import viewsets


class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all().order_by('-created_at')
    serializer_class = UserSerializer


class MessageViewSet(viewsets.modelViewSet):
    queryset = Message.objects.all().order_by('conversation', '-sent_at')
    serializer_class = MessageSerializer

    def perform_create(self, serializer):
        serializer.save(sender=self.request.user)
        
class ConversationViewSet(viewsets.ModelViewSet):
    queryset = Conversation.objects.all().order_by('-created_at')
    serializer_class = ConversationSerializer

    def perform_create(self, serializer):
        conversation = serializer.save()
        conversation.participants.add(self.request.user)