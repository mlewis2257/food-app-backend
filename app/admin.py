from django.contrib import admin
from .models import Food

# Register your models here.


class Admin(admin.ModelAdmin):
    list_display = ("title", "description", "completed")


admin.site.register(Food, Admin)
