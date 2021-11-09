from django.db import models
from core import models as core_models

# Create your models here.
class Reviw(core_models.TimeStampedModel):
    """
    Review Models Definition
    """

    review = models.TextField()
    accuracy = models.IntegerField()
    communication = models.IntegerField()
    clenliness = models.IntegerField()
    location = models.IntegerField()
    check_in = models.IntegerField()
    value = models.IntegerField()
    user = models.ForeignKey("users.User", on_delete=models.CASCADE)
    room = models.ForeignKey("rooms.Room", on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.review} - {self.room}"

    def rating_average(self):
        avg = (
            self.accuracy
            + self.communication
            + self.cleanliness
            + self.location
            + self.check_in
            + self.value
        ) / 6

        return round(avg, 2)

    rating_average.shord_description = "AVG."
