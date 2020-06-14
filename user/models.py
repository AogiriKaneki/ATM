from django.db import models

class Users(models.Model):
    name = models.CharField(max_length=20)
    card = models.SmallIntegerField()
    pin = models.SmallIntegerField()

    def __str__(self):
        return self.name