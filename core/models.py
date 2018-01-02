from django.contrib.auth.models import User
from django.db import models


# Create your models here.


def user_directory_path(instance, filename):
    # file will be uploaded to MEDIA_ROOT/user_<id>/<filename>
    return 'user_{0}/{1}'.format(instance.user.id, filename)


class Application(models.Model):
    name = models.CharField(max_length=50, null=True)
    image = models.ImageField(null=True)
    date = models.DateField(auto_now=True, null=True)


class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, null=True)
    picture = models.ImageField(upload_to=user_directory_path, null=True)
    application = models.ManyToManyField(Application, null=True)
