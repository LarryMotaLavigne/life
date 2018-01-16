from allauth.account.views import *
from django.contrib.auth.models import User
from django.shortcuts import get_object_or_404
from django.views.generic import TemplateView, UpdateView

from core import utils
from core.forms import UserForm, ProfileForm
from core.models import Profile


class IndexView(TemplateView):
    template_name = "core/index.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['login_form'] = LoginForm()
        context['signup_form'] = SignupForm()
        context["application_list"] = utils.get_available_applications()
        return context


index = IndexView.as_view()


class ProfileView(UpdateView):
    template_name = "core/profile.html"
    form_class = UserForm
    second_form_class = ProfileForm
    model = User

    @method_decorator(login_required)
    def dispatch(self, *args, **kwargs):
        return super(ProfileView, self).dispatch(*args, **kwargs)

    def get_object(self):
        return get_object_or_404(User, pk=self.request.session['_auth_user_id'])

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        if 'user_form' not in context:
            context['user_form'] = self.form_class(self.request.GET)
        if 'profile_form' not in context:
            context['profile_form'] = self.second_form_class(self.request.GET)
        context["application_list"] = utils.get_available_applications()
        return context

    def get(self, request, *args, **kwargs):
        super(ProfileView, self).get(request, *args, **kwargs)
        user_object = User.objects.get(pk=self.request.session['_auth_user_id'])
        user_form = self.form_class(initial={'first_name': user_object.first_name, 'last_name': user_object.last_name, 'email': user_object.email})
        profile_object = Profile.objects.get(user=user_object)
        profile_form = self.second_form_class(initial={'picture': profile_object.picture, 'application': profile_object.application.all()})
        return self.render_to_response(self.get_context_data(object=self.object, user_form=user_form, profile_form=profile_form))

    def post(self, request, *args, **kwargs):
        self.object = self.get_object()
        user_form = self.form_class(request.POST, instance=request.user)
        profile_form = self.second_form_class(request.POST, request.FILES, instance=request.user.profile)

        if user_form.is_valid() and profile_form.is_valid():
            userdata = user_form.save(commit=False)
            userdata.save()

            profiledata = profile_form.save(commit=False)
            profiledata.user = userdata
            profiledata.save()
            profile_form.save_m2m()

            messages.success(self.request, 'Profile saved successfully')
            return HttpResponseRedirect(self.get_success_url())
        else:
            return self.render_to_response(self.get_context_data(user_form=user_form, profile_form=profile_form))

    def get_success_url(self):
        return reverse("profile")


profile = ProfileView.as_view()
