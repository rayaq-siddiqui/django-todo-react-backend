from django.contrib import admin
from .models import ToDo


# Register your models here.
# this allows to be displayed on the admin website
class ToDoAdmin(admin.ModelAdmin):
    list_display = ('title', 'description', 'completed')

admin.site.register(ToDo, ToDoAdmin)
