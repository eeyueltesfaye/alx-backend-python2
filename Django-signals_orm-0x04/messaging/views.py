from django.shortcuts import render, get_object_or_404, redirect
from .models import Message
from django.contrib.auth.decorators import login_required
from django.contrib.auth import logout 
from django.contrib.auth.models import User
import logging
from .utils import get_threaded_replies


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