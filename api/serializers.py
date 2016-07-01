from rest_framework import serializers

#load django and webapp models
from django.contrib.auth.models import *
from api.models import *

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('id', 'username', 'email', 'url')