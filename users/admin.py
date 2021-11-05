from django.contrib import admin
from . import models
# Register your models here.
@admin.register(models.User)
class CustomUserAdmin(admin.ModelAdmin):
    list_display=('username', 'gender','language','currency','superhost')