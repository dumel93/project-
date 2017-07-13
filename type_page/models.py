from django.contrib.auth.models import AbstractUser
from django.db import models

# Create your models here.

class User(AbstractUser):
    email = models.EmailField('email address', unique=True)
    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['username']


class FootballType(models.Model):


    first_team=models.CharField(max_length=64,null=True)
    second_team=models.CharField(max_length=64, null=True)
    draw= models.BooleanField(default=False)
    is_ended=models.BooleanField(default=False)
    date_game= models.DateTimeField()
    league= models.CharField(max_length=64)
    course=models.DecimalField(max_digits=5,decimal_places=2)
    comments=models.CharField(max_length=128, null=True)
    bet=models.IntegerField()



    class Meta :
        ordering=['date_game']


    @property
    def total(self):
        if self.is_ended == True:
            if self.draw == True:
                return self.bet*(self.course-1)
            return (self.bet)*(-1)
        return self.bet*(self.course-1)


    def __str__(self):
        return "{} vs. {}".format(self.first_team, self.second_team)

