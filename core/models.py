from django.contrib.auth.models import User
from django.db import models


# Create your models here.


def user_directory_path(instance, filename):
    # file will be uploaded to MEDIA_ROOT/user_<id>/<filename>
    return 'user_{0}/{1}'.format(instance.user.id, filename)


class Application(models.Model):
    name = models.CharField(max_length=50)
    image = models.ImageField(blank=True)
    date = models.DateField(auto_now=True)


class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    picture = models.ImageField(upload_to=user_directory_path, blank=True)
    application = models.ManyToManyField(Application)
