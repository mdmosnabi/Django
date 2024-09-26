# customadmin/middleware.py

from django.shortcuts import redirect
from django.urls import reverse
from django.conf import settings

class CustomAdminAuthMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        # Check if the request is for the custom admin panel
        if request.path.startswith('/admin/'):
            # Ensure the user is authenticated and is a staff member
            if not request.user.is_authenticated or not request.user.is_staff:
                # Redirect to the login page if not authenticated or not staff
                return redirect(settings.LOGIN_URL)
        
        # Proceed with the response
        response = self.get_response(request)
        return response
