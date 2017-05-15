from django.db import models

# Create your models here.
class Map(models.Model):
    map_name = models.CharField(max_length=32)
    map_date = models.DateTimeField('published on')
    map_author = models.CharField(max_length=32)
    map_path = models.CharField(max_length=32)

    def __str__(self):
        return f'{self.map_name} - {self.map_author}/{self.map_date}'

class Scene(models.Model):
    parent_map = models.ForeignKey(Map, on_delete=models.CASCADE)
    scene_name = models.CharField(max_length=32)
    scene_background = models.CharField(max_length=32)

    def __str__(self):
        return f'{self.parent_map.map_name}/{self.scene_name} - {self.parent_map.map_author}/{self.parent_map.map_date}'

class TemplateGrid(models.Model):
    parent_scene = models.ForeignKey(Scene, on_delete=models.CASCADE)
    scene_grid = models.CharField(max_length=640)
    def __str__(self):
        return f'{self.scene_grid}'
