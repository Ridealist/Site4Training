from django.db import models

class Training(models.Model):
    title = models.CharField(max_length=200)
    website = models.CharField(max_length=50)
    type = models.CharField(max_length=50)
    description = models.TextField(blank=True, null=True)
    time = models.CharField(max_length=20)
    price = models.PositiveIntegerField()
    url = models.URLField()
    image = models.ImageField(blank=True, null=True)

    def __str__(self):
        return self.title