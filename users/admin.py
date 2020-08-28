

# Register your models here.
from django.contrib import admin

from .models import MyUser,UserType

myModels = [MyUser,UserType]
admin.site.register(myModels)

