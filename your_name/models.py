from django.db import models


class Card(models.Model):
    your_name = models.CharField(max_length=10)

    def __str__(self):
        return self.your_name
