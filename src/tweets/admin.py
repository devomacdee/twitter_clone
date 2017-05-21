from django.contrib import admin

# Register your models here.
from .models import Tweet

# register the models
admin.site.register(Tweet)
