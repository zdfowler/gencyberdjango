from rest_framework import serializers

#load django and webapp models
from django.contrib.auth.models import *
from api.models import *

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('id', 'username', 'email', 'url')

class LikeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Like
        fields = ('id', 'title', 'objid', 'farm', 'secret', 'server')

class UserprofileSerializer(serializers.ModelSerializer):
	user = UserSerializer()
	class Meta:
		model = Userprofile
		fields = ('id', 'user', 'likes')
		depth = 1