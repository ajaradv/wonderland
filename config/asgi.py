# ruff: noqa
"""
ASGI config for Alice in Wonderland project.

It exposes the ASGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/dev/howto/deployment/asgi/

"""

import os
import sys
from pathlib import Path

from channels.auth import AuthMiddlewareStack
from channels.routing import ProtocolTypeRouter, URLRouter
from channels.security.websocket import AllowedHostsOriginValidator
from django.core.asgi import get_asgi_application
from django.urls import path

from config.websocket import EchoConsumer, websocket_application

from .routing import websocket_routes

# This allows easy placement of apps within the interior
# wonderland directory.
BASE_DIR = Path(__file__).resolve(strict=True).parent.parent
sys.path.append(str(BASE_DIR / "wonderland"))

# If DJANGO_SETTINGS_MODULE is unset, default to the local settings
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "config.settings.local")

# This application object is used by any ASGI server configured to use this file.
django_application = get_asgi_application()
# Apply ASGI middleware here.
# from helloworld.asgi import HelloWorldApplication
# application = HelloWorldApplication(application)


application = ProtocolTypeRouter(
    {
        "http": django_application,
        "websocket": AllowedHostsOriginValidator(
            AuthMiddlewareStack(URLRouter(websocket_routes))
        ),
    }
)

# Import websocket application here, so apps from django_application are loaded first


# async def application(scope, receive, send):
#    if scope["type"] == "http":
#        await django_application(scope, receive, send)
#    elif scope["type"] == "websocket":
#        await websocket_application(scope, receive, send)
#    else:
#        msg = f"Unknown scope type {scope['type']}"
#        raise NotImplementedError(msg)
