from __future__ import unicode_literals

from django.db import models
from django.conf import settings
from django.contrib.auth import get_user_model


class student(models.Model):
    semester=models.CharField(default='', max_length=256)
    firstName=models.CharField(default='', max_length=256)
    lastName=models.CharField(default='', max_length=256)
    className=models.CharField(default='', max_length=256)

    def __str__(self):
        return self.userId
# student grades.
class grade(models.Model):
    user=models.ForeignKey(student, on_delete=models.CASCADE)
    grade=models.IntegerField
    def __str__(self):
        return self.userId
