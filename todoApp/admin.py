
# Import necessary modules
from django.contrib import admin
from django.contrib.admin import ModelAdmin
from .models import Todo

# Define custom admin class for Todo model
class TodoAdmin(admin.ModelAdmin):
    list_display = ('text', 'users')

# Register Todo model with custom admin class
admin.site.register(Todo, TodoAdmin)