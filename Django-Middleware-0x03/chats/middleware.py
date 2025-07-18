from datetime import datetime
import logging
import os

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
