from django.db import models


class Recipe(models.Model):
    name = models.CharField(max_length=100)
    category = models.CharField(max_length=100)
    description = models.TextField()

    def __str__(self):
        return self.name