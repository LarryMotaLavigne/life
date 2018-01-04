import os.path
from django.contrib.auth.models import User
from django.db import models


def user_upload_path(self, filename):
    # file will be uploaded to MEDIA_ROOT/user_<id>/<filename>
    return 'user_{0}/{1}'.format(self.user.id, filename)


def application_upload_path(self, filename):
    return 'application/%s%s' % (self.name, os.path.splitext(filename)[1])


class Application(models.Model):
    name = models.CharField(max_length=50, null=True)
    image = models.ImageField(blank=True, upload_to=application_upload_path)
    date = models.DateField(auto_now=True, null=True)

    def __str__(self):
        return self.name


class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, null=True)
    picture = models.ImageField(upload_to=user_upload_path, null=True)
    application = models.ManyToManyField(Application)

    def __str__(self):
        return self.user.username
