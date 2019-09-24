from django.db import models

# Create your models here.

class Player(models.Model):
    user_uuid = models.IntegerField()
    username = models.CharField(max_length=10000)
    password = models.CharField(max_length=10000)
    has_active_session = models.BooleanField(default=False)
    friends = models.ForeignKey("self", on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.user_uuid} {self.username}" 


class Session(models.Model): 
    session_uuid = models.IntegerField()
    session_status = models.CharField(max_length=10000)
    players = models.ManyToManyField(Player)
