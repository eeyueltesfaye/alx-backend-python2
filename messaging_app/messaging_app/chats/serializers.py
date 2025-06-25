from rest_framework import serializers
from .models import User, Conversation, Message

class UserSerializer(serializers.ModelSerializer):
    username = serializers.CharField(max_length=150)
    email = serializers.EmailField()

    class Meta:
        model = User
        fields = ['user_id', 'username', 'email', 'first_name', 'last_name', 'phone_number', 'is_online', 'created_at']
        read_only_fields = ['user_id', 'created_at']

    def validate_username(self, value):
        """
        Validate username field with custom validation.
        """
        if len(value) < 3:
            raise serializers.ValidationError("Username must be at least 3 characters long.")
        return value
    
    def validate_email(self, value):
        """
        Validate email field with custom validation.
        """
        if User.objects.filter(email=value).exists():
            raise serializers.ValidationError("A user with this email already exists.")
        return value
    

class MessageSerializer(serializers.ModelSerializer):
    sender = UserSerializer(read_only = True)
    short_message = serializers.SerializerMethodField()

    class Meta:
        model = Message
        fields = ['message_id', 'sender', 'message_body', 'sent_at', 'timestamp', 'is_read', ' short_message']

    def get_short_message(self, obj):
        # Return the first 20 characters of the message body
        return obj.message_body[:20]

    def validate_message_body(self, value):
   #raise errors if the message body is empty
        if not value.strip():
            raise serializers.ValidationError("Message body cannot be empty.")
        return value

class ConversatiionSerializer(serializers.ModelSerializer):
     participants = UserSerializer(many=True, read_only=True)
     messages = MessageSerializer(many=True, read_only=True)

     class Meta:
        model = Conversation
        fields = ['conversation_id', 'title', 'participants', 'messages', 'created_at', 'updated_at']
        read_only_fields = ['conversation_id', 'created_at', 'updated_at']