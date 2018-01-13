import os.path
from django.contrib.auth.models import User
from django.db import models
from django.db.models.signals import post_save
from django.dispatch import receiver


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


@receiver(post_save, sender=User)
def create_user_profile(sender, instance, created, **kwargs):
    if created:
        Profile.objects.create(user=instance)


@receiver(post_save, sender=User)
def save_user_profile(sender, instance, **kwargs):
    instance.profile.save()