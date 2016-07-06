from __future__ import unicode_literals

from django.db import models
from django.contrib.auth.models import *
from django.contrib import admin

# Create your models here.
class Like(models.Model):
	user =  models.ForeignKey(User)
	title = models.CharField(max_length=100, blank=False)
	objid = models.IntegerField(blank=False)
	farm = models.CharField(max_length=100, blank=False)
	secret = models.CharField(max_length=100, blank=False)
	server = models.CharField(max_length=100, blank=False)

	def __str__(self):
		return self.title

	class Admin(admin.ModelAdmin):
		list_display = ('title', 'objid', 'user')
	
class Userprofile(models.Model):
	user = models.ForeignKey(User)
	likes = models.ManyToManyField(Like)

	def __str__(self):
		return self.user.username

	class Admin(admin.ModelAdmin):
		list_display = ('user',)