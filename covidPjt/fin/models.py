from django.db import models
from django.forms import CharField


# Create your models here.

class Covid(models.Model):
    date= models.CharField(max_length=30, primary_key=True)
    intdate= models.IntegerField(default=0)
    deathCnt = models.IntegerField( default=0)
    decideCnt= models.IntegerField( default=0)

    def __str__(self):
        return self.date
