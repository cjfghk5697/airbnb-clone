from django.contrib import admin
from . import models

# Register your models here.


@admin.register(models.Reservations)
class RservationAdmin(admin.ModelAdmin):
    """
    Reservation Admin Definition
    """

    pass
