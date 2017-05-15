from django.db import models

# Create your models here.
class Map(models.Model):
    map_name = models.CharField(max_length=64)
    map_date = models.DateTimeField('published on')
    map_author = models.CharField(max_length=32)

    def __str__(self):
        return f'{self.map_name} - {self.map_author}/{self.map_date}'