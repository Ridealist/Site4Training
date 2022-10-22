from django.db import models
from django.contrib.auth.models import User

class Training_List(models.Model):
    owner = models.ForeignKey(User, related_name="owner", on_delete=models.CASCADE)
    number = models.CharField(max_length=400)
    name = models.CharField(max_length=300)
    auth = models.CharField(max_length=200)
    period_st = models.DateField()
    period_end = models.DateField()
    time = models.DurationField()
    type = models.CharField(max_length=100)

    def __str__(self):
        return self.name


class Excel_File(models.Model):
    owner = models.ForeignKey(User, on_delete=models.CASCADE)
    upload = models.FileField(upload_to='uploads/')