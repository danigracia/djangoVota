import datetime

from django.db import models
from django.utils import timezone


class Question(models.Model):
    question_text = models.CharField(max_length=200)
    pub_date = models.DateTimeField('Fecha inicio   ')
    end_date = models.DateTimeField('Fecha final')
    def __str__(self):
            return self.question_text

    def was_published_recently(self):
            return self.pub_date >= timezone.now() - datetime.timedelta(days=1)

    def was_published_end(self):
            return self.end_date >= timezone.now() - datetime.timedelta(days=1)


class Choice(models.Model):
    pregunta = models.ForeignKey(Question, on_delete=models.CASCADE)
    choice_text = models.CharField(max_length=200)
    votes = models.IntegerField(default=0)
    def __str__(self):
            return self.choice_text