from django.shortcuts import render
from django.shortcuts import render, get_object_or_404
from .models import Message

def message_detail(request, pk):
    message = get_object_or_404(Message, pk=pk)
    history = message.history.all()
    return render(request, 'messaging/message_detail.html', {
        'message': message,
        'history': history,
    })

