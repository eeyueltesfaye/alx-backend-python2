# 📨 Django Messaging App

This project is a private messaging system built with Django. It allows users to send messages, reply to specific messages in threads, delete their accounts along with related data, and more. The app demonstrates advanced Django ORM techniques, custom managers, and basic caching for improved performance.

## 🚀 Features

- 🔒 User Authentication – Secure login and logout functionality.
- 🧵 Threaded Conversations – Reply to specific messages using parent-child relationships.
- 🔔 Notifications Support – (Extendable) placeholder for real-time or async notifications.
- 🗑️ User Deletion with Signals – Automatically clean up related messages and histories when a user deletes their account.
- 📬 Unread Messages Manager – Custom ORM manager to fetch only unread messages.
- ⚡ View-Level Caching – Improve performance by caching message list views using `cache_page`.

## 🛠️ Tech Stack

- Backend: Django (Python)
- Database: SQLite (for development)
- Cache: LocMemCache (in-memory caching)
- Templates: Django Templating Engine (no API used)

## 📁 Project Structure

messaging_project/
│
├── messaging/                # Messaging app
│   ├── models.py             # Message model, custom manager
│   ├── views.py              # All message views including caching
│   ├── signals.py            # Signal handlers for user deletion
│   ├── templates/messaging/  # Templates (minimal UI)
│   ├── urls.py               # App-level URLs
│   └── ...
│
├── messaging_project/settings.py  # Main Django settings (includes cache setup)
├── messaging_project/urls.py      # Project-level URLs
└── ...

## ⚙️ Setup Instructions

1. Clone the Repo

   git clone put url
   cd to the project

2. Install Dependencies

   pip install -r requirements.txt

3. Run Migrations

   python manage.py migrate

4. Create Superuser

   python manage.py createsuperuser

5. Start the Server

   python manage.py runserver

6. Access the App

   http://127.0.0.1:8000/

## 💡 Key Features Explained

### ✅ Delete User with Signals

- View: delete_user(request)
- Signal: post_delete removes related messages and histories
- Template: account_deleted.html confirms deletion

### ✅ Threaded Conversations

- Message model includes parent_message = models.ForeignKey('self', null=True, ...)
- Replies are nested using a recursive query for easy threading

### ✅ Unread Messages Manager

class UnreadMessagesManager(models.Manager):
    def for_user(self, user):
        return self.filter(recipient=user, read=False).only('sender', 'subject', 'timestamp')

### ✅ View-Level Caching

- Decorator used: @cache_page(60)
- Set up in settings.py:

CACHES = {
    'default': {
        'BACKEND': 'django.core.cache.backends.locmem.LocMemCache',
        'LOCATION': 'unique-snowflake',
    }
}

## 🔍 Testing Caching

- Visit a conversation URL
- Refresh it within 60 seconds → View isn't re-executed (check logs or console print)
- Clear the cache manually:

from django.core.cache import cache
cache.clear()

## 📌 Future Improvements

- Add WebSocket support for real-time updates
- Use Redis for production-level caching
- Implement search and filtering
- Add unit tests

