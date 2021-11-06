from django.db import models

# Create your models here.

class TimeStampedModel(models.Model):
    '''
    Time Stamped Model
    '''
    created=models.DateTimeField(auto_now_add=True)
    updataed= models.DateTimeField(auto_now=True)
    class Meta:
        abstract = True