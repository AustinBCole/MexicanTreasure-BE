from django.db import models

# Create your models here.

class Player(models.Model) {
    user_uuid = models.IntegerField()
    username = models.CharField(max_length=None)
    password = models.CharField(max_length=None)
    has_active_session = models.BooleanField(default=False)

    def __str__(self):
        return f"{username} {user_uuid}" 
}

class Session(models.Model) {
    session_uuid = models.IntegerField()
    session_status = models.CharField(max_length=None)
    players = models.ManyToManyField(Player)

}