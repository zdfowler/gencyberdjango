from django.shortcuts import *

# Import models
from django.db import models
from django.contrib.auth.models import *
from api.models import *

#REST API
from rest_framework import viewsets
from api.serializers import *
from django.http import Http404
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

from django.contrib.auth import authenticate, login, logout
from rest_framework.permissions import *
from rest_framework.decorators import *

class UserViewSet(viewsets.ModelViewSet):
	"""
	API endpoint that allows users to be viewed.
	"""
	queryset = User.objects.all()
	serializer_class = UserSerializer

class LikeViewSet(viewsets.ModelViewSet):
	"""
	API endpoint that allows users to be viewed.
	"""
	queryset = Like.objects.all()
	serializer_class = LikeSerializer

class UserprofileViewSet(viewsets.ModelViewSet):
	"""
	API endpoint that allows users to be viewed.
	"""
	queryset = Userprofile.objects.all()
	serializer_class = UserprofileSerializer