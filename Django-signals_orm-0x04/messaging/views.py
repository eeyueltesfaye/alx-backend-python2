from django.shortcuts import render, get_object_or_404, redirect
from .models import Message
from django.contrib.auth.decorators import login_required
from django.contrib.auth import logout 
from django.contrib.auth.models import User
import logging
from .utils import get_threaded_replies
from django.http import JsonResponse
from django.views.decorators.cache import cache_page



def message_detail(request, pk):
    message = get_object_or_404(Message, pk=pk)
    history = message.history.all()
    return render(request, 'messaging/message_detail.html', {
        'message': message,
        'history': history,
    })

logger = logging.getLogger(__name__)

@login_required
def delete_user(request):
    if request.method == "POST":
        user = request.user
        logger.info(f"Deleting user: {user.username} (ID: {user.id})")  # Logging
        logout(request)  # Log out first
        user.delete()
        return redirect("account_deleted")  # Redirect to goodbye page
    return render(request, 'messaging/delete_account.html')


def account_deleted(request):
    return render(request, 'messaging/account_deleted.html')


def get_message_thread(message_id):
    message = get_object_or_404(Message.objects.select_related('sender', 'receiver'), pk=message_id)
    thread = get_threaded_replies(message)
    return {
        "message": message,
        "thread": thread
    }

@login_required
def unread_messages_view(request):
    user = request.user
    unread = Message.unread.for_user(user)
    data = [
        {
            "id": msg.id,
            "sender": msg.sender.username,
            "content": msg.content,
            "timestamp": msg.timestamp
        } for msg in unread
    ]
    return JsonResponse(data, safe=False)

@cache_page(60)  # Cache this view for 60 seconds
@login_required
def conversation_messages(request, username):
    user = request.user
    other_user = get_object_or_404(User, username=username)

    messages = Message.objects.filter(
        sender__in=[user, other_user],
        receiver__in=[user, other_user]
    ).order_by('timestamp')

    data = [
        {
            "id": m.id,
            "sender": m.sender.username,
            "receiver": m.receiver.username,
            "content": m.content,
            "timestamp": m.timestamp
        } for m in messages
    ]

    return JsonResponse(data, safe=False)