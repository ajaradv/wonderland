from django.urls import path

from .views import chat_index

app_name = "chat"

urlpatterns = [
    path("room", view=chat_index, name="index"),
]
