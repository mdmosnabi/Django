"""
import os

from django.core.asgi import get_asgi_application

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'ecommpro.settings')

application = get_asgi_application()
"""
import os
from channels.auth import AuthMiddlewareStack
from channels.routing import ProtocolTypeRouter, URLRouter
from django.core.asgi import get_asgi_application
import Support.routing

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'ecommpro.settings')

application = ProtocolTypeRouter({
    "http": get_asgi_application(),
    "websocket": AuthMiddlewareStack(
        URLRouter(
            Support.routing.websocket_urlpatterns
        )
    ),
})

