from django.contrib import admin
from .models import *
# Register your models here.
@admin.register(Todo)
class AdminView(admin.ModelAdmin):
    pass
