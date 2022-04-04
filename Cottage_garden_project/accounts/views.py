from django.contrib.auth.views import PasswordChangeView
from django.contrib.auth import views as auth_views
from django.urls import reverse_lazy
from django.views.generic import CreateView, DetailView
from Cottage_garden_project.accounts.models import GardenPlantsUser, Profile
from Cottage_garden_project.accounts.forms import CreateProfileForm
from Cottage_garden_project.common.mixin import RedirectToDashboard
from Cottage_garden_project.main.models import Garden, Plant


class UserRegistrationView(RedirectToDashboard, CreateView):
    model = GardenPlantsUser
    form_class = CreateProfileForm
    template_name = 'accounts/profile_create.html'
    success_url = reverse_lazy('dashboard')


class UserLoginView(auth_views.LoginView):
    template_name = 'accounts/login_page.html'
    success_url = reverse_lazy('dashboard')

    def get_success_url(self):
        if self.success_url:
            return self.success_url
        return super().get_success_url()


class ProfileDetailsView(DetailView):
    model = Profile
    template_name = 'accounts/profile_details.html'
    # context_object_name = 'profile'


    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        # self.object is a Profile instance
        gardens = list(Garden.objects.filter(user_id=self.object.user_id))
        plants = list(Plant.objects.filter(user_id=self.object.user_id))

        total_plants_count = len(plants)
        total_gardens_count = len(gardens)

        context.update({
            'total_plants_count': total_plants_count,
            'total_gardens_count': total_gardens_count,
            'is_owner': self.object.user_id == self.request.user.id,

        })

        return context


class EditProfileView:
    pass


class ChangeUserPasswordView(PasswordChangeView):
    template_name = 'accounts/change_password.html'

