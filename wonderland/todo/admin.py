from django.contrib import admin
from unfold.admin import ModelAdmin

from .models import Todo

# Register your models here.


@admin.register(Todo)
class TodoAdmin(ModelAdmin):
    pass
