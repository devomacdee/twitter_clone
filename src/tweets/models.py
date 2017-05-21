from django.db import models
from django.conf import settings
from .validators import validate_content

# Create your models here.

class Tweet(models.Model):
    """model for a tweet"""

    user      = models.ForeignKey(settings.AUTH_USER_MODEL)
    content   = models.CharField(max_length=140, validators=[validate_content])
    timestamp = models.DateTimeField(auto_now_add=True)
    updated   = models.DateTimeField(auto_now=True)

    def __str__(self):
        return str(self.content)

    # model validation
    # def clean(self, *args, **kwargs):
        # content = self.content
        # if content == "abc":
        #     raise ValidationError("Cannot be ABC")
        # return super(Tweet, self).clean(*ags, **kwargs)
