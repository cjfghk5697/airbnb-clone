from django.contrib import admin
from . import models

# Register your models here.


@admin.register(models.Reviw)
class ReviewAdmin(admin.ModelAdmin):
    """
    Review Admin Definition
    """

    pass
