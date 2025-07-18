from datetime import datetime, time     # time here is datetime.time
import logging
import os
from django.http import HttpResponseForbidden
import time as time_module 

class RequestLoggingMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response
        # Configure logging only once
        log_path = os.path.join(os.path.dirname(__file__), '../requests.log')
        logging.basicConfig(
            filename=log_path,
            level=logging.INFO,
            format='%(message)s'
        )

    def __call__(self, request):
        user = request.user if request.user.is_authenticated else 'Anonymous'
        log_message = f"{datetime.now()} - User: {user} - Path: {request.path}"
        logging.info(log_message)
        return self.get_response(request)


class RestrictAccessByTimeMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        # Define the allowed time range: 6 PM to 9 PM
        now = datetime.now().time()
        start_time = time(18, 0)  # 6:00 PM
        end_time = time(21, 0)    # 9:00 PM

        # Restrict access only to chat paths 
        if request.path.startswith("/api/") or request.path.startswith("/api/conversations/"):
            if not (start_time <= now <= end_time):
                return HttpResponseForbidden("Access to chat is only allowed between 6 PM and 9 PM.")

        return self.get_response(request)
    

class OffensiveLanguageMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response
        self.request_log = {}  # { ip: [timestamp1, timestamp2, ...] }

    def __call__(self, request):
        if request.method == 'POST' and request.path.startswith('/api/conversations/'):
            ip = self.get_client_ip(request)
            now = time_module.time()

            # Clean up old entries
            if ip not in self.request_log:
                self.request_log[ip] = []

            # Keep only timestamps within last 60 seconds
            self.request_log[ip] = [t for t in self.request_log[ip] if now - t < 60]

            if len(self.request_log[ip]) >= 5:
                return HttpResponseForbidden("Message limit exceeded. Try again after a minute.")

            # Log this new request
            self.request_log[ip].append(now)

        return self.get_response(request)

    def get_client_ip(self, request):
        # Handle proxy headers if applicable
        x_forwarded_for = request.META.get('HTTP_X_FORWARDED_FOR')
        if x_forwarded_for:
            return x_forwarded_for.split(',')[0]
        return request.META.get('REMOTE_ADDR')


class RolePermissionMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        # Check only chat-related endpoints
        if request.path.startswith("/admin/"):
            # 🔍 Debug: Check who Django thinks the user is
            print("Is authenticated:", request.user.is_authenticated)
            print("User:", request.user)
            print("Is staff:", request.user.is_staff)
            print("Is superuser:", request.user.is_superuser)

            user = request.user
            if not user.is_authenticated:
                return HttpResponseForbidden("You must be logged in.")

            # Use this if you have `role` field
            # if user.role not in ['admin', 'moderator']:
            #     return HttpResponseForbidden("Only admins or moderators can access this feature.")

            # Or use Django's built-in roles
            if not (user.is_staff or user.is_superuser):
                return HttpResponseForbidden("Only admins or moderators can access this feature.")

        return self.get_response(request)