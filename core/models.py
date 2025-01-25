from django.db import models

# Create your models here.

class Match(models.Model):
    team1= models.CharField(max_length=100)
    team2= models.CharField(max_length=100)
    score_team1=models.IntegerField(default=0)
    score_team2=models.IntegerField(default=0)
    start_time=models.DateTimeField()
    end_time=models.DateTimeField(null=True, blank=True)
    is_live=models.BooleanField(default=True)

    def __str__(self):
        return f"{self.team1} vs {self.team2} at {self.start_time}"
    
