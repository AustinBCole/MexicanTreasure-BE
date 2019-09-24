from rest_framework.serializers import ModelSerializer

from .models import Player

class PlayerSerializer(HyperLinkedModelSerializer):
    class Meta:
        model = Player
        fields = ['username', 'user_uuid', 'password']