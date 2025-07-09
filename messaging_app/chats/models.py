from django.db import models
from django.contrib.auth.models import AbstractUser
import uuid 
from django.conf import settings


class User(AbstractUser):
    user_id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    email = models.EmailField(max_length=255, null=False, unique=True)
    password = models.CharField(max_length=128)  # Explicitly define password field
    first_name = models.CharField(max_length=30, blank=True)
    last_name = models.CharField(max_length=30, blank=True)
    phone_number = models.CharField(max_length=15, blank=True)
    is_online = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.username 

class Conversation(models.Model):
    conversation_id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    title = models.CharField(max_length=255, null=False)
    participants = models.ManyToManyField(settings.AUTH_USER_MODEL,
        related_name='conversations',
        help_text="Users participating in this conversation")
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ['-updated_at']

    def __str__(self):
        participant_names = ', '.join([user.username for user in self.participants.all()[:3]])
        if self.participants.count() > 3:
            participant_names += f' and {self.participants.count() - 3} others'
        return f"Conversation: {participant_names}"

    

class Message(models.Model):
     message_id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
     sender = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        related_name='sent_messages',
        help_text="User who sent this message"
    )
     conversation = models.ForeignKey(
        Conversation,
        on_delete=models.CASCADE,
        related_name='messages',
        help_text="Conversation this message belongs to"
    )
     message_body = models.TextField(help_text="Message content")
     sent_at = models.DateTimeField(auto_now_add=True)
     timestamp = models.DateTimeField(auto_now_add=True)
     is_read = models.BooleanField(default=False)

     class Meta:
            ordering = ['-timestamp']

     def __str__(self):
            return f"{self.sender.username}: {self.message_body[:50]}{'...' if len(self.message_body) > 50 else ''}"

     def save(self, *args, **kwargs):
            """Update conversation's updated_at when a new message is added"""
            super().save(*args, **kwargs)
            self.conversation.save()  # This will update the updated_at field