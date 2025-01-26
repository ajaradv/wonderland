from django.urls import path

from .views import complete_todo
from .views import delete_todo
from .views import index
from .views import submit_todo

app_name = "todo"
urlpatterns = [
    path("", view=index, name="index"),
    path("submit-todo", view=submit_todo, name="submit-todo"),
    path("complete-todo/<int:pk>", view=complete_todo, name="complete-todo"),
    path("delete-todo/<int:pk>", view=delete_todo, name="delete-todo"),
]
