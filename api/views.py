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

class Session(APIView):
	permission_classes = (AllowAny,)
	def form_response(self, isauthenticated, userid, username, error=""):
		data = {
			'isauthenticated': isauthenticated,
			'userid': userid,
			'username': username
		}
		if error:
			data['message'] = error

		return Response(data)

	def get(self, request, *args, **kwargs):
		# Get the current user
		if request.user.is_authenticated():
			return self.form_response(True, request.user.id, request.user.username)
		return self.form_response(False, None, None)

	def post(self, request, *args, **kwargs):
		# Login
		username = request.POST.get('username')
		password = request.POST.get('password')
		user = authenticate(username=username, password=password)
		if user is not None:
			if user.is_active:
				login(request, user)
				return self.form_response(True, user.id, user.username)
			return self.form_response(False, None, None, "Account is suspended")
		return self.form_response(False, None, None, "Invalid username or password")

	def delete(self, request, *args, **kwargs):
		# Logout
		logout(request)
		return Response(status=status.HTTP_204_NO_CONTENT)



def home(request):
	"""
	Send requests to / to the ember.js clientside app  """

	return render_to_response('index.html',
		{}, RequestContext(request))

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