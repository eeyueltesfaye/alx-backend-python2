def get_threaded_replies(message):
    replies = message.replies.select_related('sender').all()
    threaded = []
    for reply in replies:
        threaded.append({
            "message": reply,
            "replies": get_threaded_replies(reply)
        })
    return threaded
