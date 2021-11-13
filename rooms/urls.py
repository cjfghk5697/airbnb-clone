from django.urls import path
from . import views

app_name = "rooms"

urlpatters = [
    path("<int:pk>", views.RoomDetail.as_view(), name="detail"),
    path("search/", views.search, name="search"),
]
