from django.db import models


class Calendar(models.Model):
    DoesNotExist = None
    objects = None
    year = models.IntegerField()
    month = models.IntegerField()
    day = models.IntegerField()

    def __str__(self):
        return f"{self.year}-{self.month}-{self.day}"
