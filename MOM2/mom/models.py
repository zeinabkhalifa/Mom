from django.db import models
from django.contrib.auth.models import User

class Judge(models.Model):
    account = models.ForeignKey(User, unique=True)

class Poster(models.Model):
    name = models.CharField(max_length=200)
    grades = models.IntegerField()
    isGraded = models.BooleanField(default=False)
    def __str__(self):
        return 'id:%s' %(self.id)
class Ratings(models.Model):
    judge = models.ForeignKey(Judge)
    poster = models.ForeignKey(Poster)

