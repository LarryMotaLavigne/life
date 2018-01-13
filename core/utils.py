from django.http import JsonResponse

from core.models import Application
from life import urls


class AjaxableResponseMixin:
    """
    Mixin to add AJAX support to a form.
    Must be used with an object-based FormView (e.g. CreateView)
    """
    def form_invalid(self, form):
        response = super().form_invalid(form)
        if self.request.is_ajax():
            return JsonResponse(form.errors, status=400)
        else:
            return response

    def form_valid(self, form):
        # We make sure to call the parent's form_valid() method because
        # it might do some processing (in the case of CreateView, it will
        # call form.save() for example).
        response = super().form_valid(form)
        if self.request.is_ajax():
            data = {
                'pk': self.object.pk,
            }
            return JsonResponse(data)
        else:
            return response


def get_available_applications():
    """
    Display every app in the Django project (except the core app, admin and debug_toolbar)
    :return: A list of every "application" available in the software
    """
    app_list = []
    default_blacklist = ['index', 'render_panel']
    for urlpatterns in urls.urlpatterns:
        if hasattr(urlpatterns.urlconf_name, 'urlpatterns'):  # Prevent infinite loop because the origin url is always present
            app_name = urlpatterns.urlconf_name.urlpatterns[0].name
            if app_name not in default_blacklist:
                app_list.append(app_name)
    return Application.objects.filter(name__in=app_list)
