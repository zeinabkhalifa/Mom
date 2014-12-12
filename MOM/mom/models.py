from django.db import models

class Judge(models.Model):
    account = models.ForeignKey(User, unique=True)

class Poster(models.Model):
    name = models.CharField(max_length=200)
    grades = models.IntegerField()
    isGraded = models.BooleanField(initial=False)
    def __str__(self):
        return 'id:%s' %(self.id)


