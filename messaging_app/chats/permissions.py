from rest_framework import permissions 
from rest_framework.permissions import BasePermission, SAFE_METHODS


class IsParticipantOfConversation(BasePermission):
    """
    Custom permission: 
    - Only authenticated users
    - Only participants (sender or receiver) can access a message
    """

    def has_permission(self, request, view):
        return request.user and request.user.is_authenticated

    def has_object_permission(self, request, view, obj):
        # Assumes obj is a Message instance with sender and receiver fields
        return obj.sender == request.user or obj.receiver == request.user