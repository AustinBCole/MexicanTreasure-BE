from rest_framework import serializers, viewsets, permissions
from .models import Player, Session

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

class SessionSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Session
        fields = '__all__'
        
    def create(self, validated_data):
        session = Session.objects.create(**validated_data)
        return session
        
    def post(self):
        return "Hello"

class SessionViewSet(viewsets.ModelViewSet):
    serializer_class = SessionSerializer
    queryset = Session.objects.all()
    permission_classes = [
        permissions.AllowAny
    ]