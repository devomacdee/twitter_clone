from django.contrib import admin

# Register your models here.
from .forms import TweetModelForm
from .models import Tweet

# register the models
# admin.site.register(Tweet)

class TweetModelAdmin(admin.ModelAdmin):
    form = TweetModelForm
    
admin.site.register(Tweet, TweetModelAdmin)
