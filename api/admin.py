from django.contrib import admin
from api.models import *

# Register your models here.
admin.site.register(Like, Like.Admin)
admin.site.register(Userprofile, Userprofile.Admin)