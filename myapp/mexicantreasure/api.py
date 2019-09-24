from rest_framework import serializers, viewsets, permissions
from .models import Player

class PlayerSerializer(serializers.HyperlinkedModelSerializer):

    class Meta:
        model = Player
        fields = ('username', 'password', 'user_uuid')
        
    def create(self, validated_data):
        player = Player.objects.create(**validated_data)
        return player

    def post(self):
        return "Hello"

class PlayerViewSet(viewsets.ModelViewSet):
    serializer_class = PlayerSerializer
    queryset = Player.objects.all()
    permission_classes = [
        permissions.AllowAny
    ]