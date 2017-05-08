import datetime

from django.db import models
from django.utils import timezone


class Question(models.Model):
    question_text = models.CharField(max_length=200)
    pub_date = models.DateTimeField('date published')

    def __str__(self):
        return self.question_text

    def was_published_recently(self):
        now = timezone.now()
        return now - datetime.timedelta(days=1) <= self.pub_date <= now
    was_published_recently.admin_order_field = 'pub_date'
    was_published_recently.boolean = True
    was_published_recently.short_description = 'Published recently?'

class Choice(models.Model):
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    choice_text = models.CharField(max_length=200)
    votes = models.IntegerField(default=0)

    def __str__(self):
        return self.choice_text

class Scene(models.Model):
    create_date = models.DateTimeField('published on')
    scene_name = models.CharField(max_length=64, default='scene')
    scene_author = models.CharField(max_length=16, default='anonymous')

    def __str__(self):
        return f'\'{self.scene_name}\' - by {self.scene_author}'

    def was_published_recently(self):
        return self.create_date >= timezone.now()-datetime.timedelta(days=30)
