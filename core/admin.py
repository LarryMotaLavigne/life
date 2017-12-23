from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from django.contrib.auth.models import User
from django.contrib.sites.models import Site

from .models import Application, Profile

# Register your models here.
admin.site.register(Application)
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
    list_display = ('username', 'email', 'first_name', 'last_name', 'is_staff', 'get_image')
    list_select_related = ('profile',)

    def get_image(self, instance):
        return instance.profile.picture

    get_image.short_description = 'Picture'

    def get_inline_instances(self, request, obj=None):
        if not obj:
            return list()
        return super(CustomUserAdmin, self).get_inline_instances(request, obj)


admin.site.unregister(User)
admin.site.register(User, CustomUserAdmin)
