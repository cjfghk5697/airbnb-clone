from django.db import models
from django.db.models.deletion import CASCADE
from core import models as core_models

# Create your models here.
class List(core_models.TimeStampedModel):
    """
    List Model Definition
    """
    name=models.CharField(max_length=80)
    user = models.ForeignKey("users.User",on_delete=CASCADE)
    rooms = models.ManyToManyField("rooms.Room", blank=True)

    def __str__(self):
        return self.name