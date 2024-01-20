from django.db import models
from django.contrib.auth.models import User
from django.db.models import Avg


class Restaurant(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=255, unique=True)
    place = models.TextField()
    type = models.CharField(max_length=255)

    @property
    def average_evaluation(self):
        if hasattr(self, '_average_evaluation'):
            return self._average_evaluation
        return self.visit_set.aggregate(Avg('evaluation'))

    def __str__(self):
        return self.name


class Visit(models.Model):
    restaurant = models.ForeignKey(Restaurant, on_delete=models.CASCADE)
    date_of_visit = models.DateField()
    expense = models.IntegerField()
    note = models.TextField()

    class Evaluation(models.IntegerChoices):
        BAD = 1, "Bad"
        NOT_GOOD = 2, "Not good"
        NORMAL = 3, "Normal"
        GOOD = 4, "Good"
        VERY_GOOD = 5, "Very good"

    evaluation = models.SmallIntegerField(default=Evaluation.BAD, choices=Evaluation.choices)
