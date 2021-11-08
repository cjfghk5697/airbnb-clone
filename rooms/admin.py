from django.contrib import admin
from django.contrib.admin.options import HORIZONTAL
from . import models

# Register your models here.


@admin.register(models.RoomType, models.Facility, models.Amenity, models.HouseRule)
class ItemAdmin(admin.ModelAdmin):
    """
    Item Admin Definition"""

    pass


@admin.register(models.Room)
class RoomAdmin(admin.ModelAdmin):
    """Room Admin Definition"""

    fieldsets = (
        ("Spaces", {"fields": ("guests", "beds", "bedrooms", "baths",)})(
            "Basic Info",
            {
                "fields": (
                    "name",
                    "description",
                    "country",
                    "address",
                    "price",
                )
            },
        ),
        (
            "Times",
            {
                "fields": (
                    "check_in",
                    "check_out",
                    "instant_book",
                )
            },
        ),
        (
            "More About the Space",
            {
                "fields": (
                    "amenities",
                    "facilities",
                    "house_rules",
                )
            },
        ),
        ("Last Details", {"fields": ("host",)}),
    )
    list_disply = (
        "name",
        "country",
        "city",
        "price",
        "guests",
        "beds",
        "bedrooms",
        "baths",
        "check_in",
        "check_out",
        "instant_book",
    )
    list_filter = (
        "isntant_book",
        "host__superhost",
        "room_type",
        "amenities",
        "facilites",
        "house_rules",
        "city",
        "country",
    )

    search_filter = ("=city", "^host__username")
    filter_horizontal = ("amenities", "facilities", "house_rules")


@admin.register(models.Photo)
class PhotoAdmin(admin.ModelAdmin):
    """Photo Admin Definition"""

    pass
