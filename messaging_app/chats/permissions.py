from rest_framework import permissions 


class ISOwner(permissions.BasePermission):
    """
    Allow access only if the user is accessing their own data.
    """

    def has_object_permission(self, request, view, obj):
        return obj.sender == request.user or obj.receiver == request.user
