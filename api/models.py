from __future__ import unicode_literals

from django.db import models
from django.contrib.auth.models import *

# Create your models here.
class Like(models.Model):
	title = models.CharField(max_length=100, blank=False)
	objid = models.IntegerField(blank=False)
	farm = models.CharField(max_length=100, blank=False)
	secret = models.CharField(max_length=100, blank=False)
	server = models.CharField(max_length=100, blank=False)

class Userprofile(models.Model):
	user = models.ForeignKey(User)
	likes = models.ManyToManyField(Like)
