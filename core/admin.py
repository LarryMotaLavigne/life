from django.contrib import admin
from django.contrib.admin.templatetags.admin_list import _boolean_icon
from django.contrib.auth.admin import UserAdmin
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.contrib.sites.models import Site

from .models import Application, Profile

# Register your models here.
admin.site.unregister(Site)


@admin.register(Site)
class Sites(admin.ModelAdmin):
    list_display = ["id", "domain", "name"]


class ProfileInline(admin.StackedInline):
    model = Profile
    can_delete = False
    verbose_name_plural = "Profile"
    fk_name = 'user'


class CustomUserAdmin(UserAdmin):
    inlines = (ProfileInline,)
    list_display = ('username', 'email', 'first_name', 'last_name', 'is_staff', 'get_image', 'get_application_list')
    list_select_related = ('profile',)

    def get_image(self, instance):
        return instance.profile.picture

    get_image.short_description = 'Picture'

    def get_application_list(self, instance):
        return instance.profile.application.name

    get_application_list.short_description = 'Applications'

    def get_inline_instances(self, request, obj=None):
        if not obj:
            return list()
        return super(CustomUserAdmin, self).get_inline_instances(request, obj)


admin.site.unregister(User)
admin.site.register(User, CustomUserAdmin)


@admin.register(Application)
class ApplicationAdmin(admin.ModelAdmin):
    list_display = ["id", "name", "date", "is_there_any_image"]

    def is_there_any_image(self, obj):
        if obj.image is None:
            return _boolean_icon(True)
        return _boolean_icon(False)
    is_there_any_image.short_description = "Is there any image attached ?"


admin.site.login = login_required(admin.site.login)  # Force login to access administration pages (with AllAuth)
admin.site.site_header = "Life Administration"
admin.site.site_title = "Life Administration"
