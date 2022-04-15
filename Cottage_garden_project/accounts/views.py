from django.contrib.auth.forms import PasswordChangeForm
from django.contrib.auth import views as auth_views, logout, update_session_auth_hash
from django.contrib import messages
from django.http import HttpRequest
from django.shortcuts import redirect, render
from django.urls import reverse_lazy
from django.views import generic
from django.views.generic import CreateView, DetailView, TemplateView
from Cottage_garden_project.accounts.models import GardenPlantsUser, Profile
from Cottage_garden_project.accounts.forms import CreateProfileForm
from Cottage_garden_project.common.mixin import RedirectToDashboard



class UserRegistrationView(RedirectToDashboard, CreateView):
    model = GardenPlantsUser
    form_class = CreateProfileForm
    template_name = 'accounts/profile_create.html'
    success_url = reverse_lazy('dashboard')


class UserEditView(generic.UpdateView):
    model = GardenPlantsUser
    form_class = CreateProfileForm
    template_name = 'accounts/profile_edit.html'
    success_url = reverse_lazy('dashboard')

    def has_permission(self, request):
        return request.user.is_active and request.user.is_staff

    # def get_object(self, queryset=None):
    #     return get_object_or_404(self.model, pk=self.request.user.pk)


    def get_object(self):
        return self.request.user


class UserLoginView(auth_views.LoginView):
    template_name = 'accounts/login_page.html'
    success_url = reverse_lazy('dashboard')

    def get_success_url(self):
        if self.success_url:
            return self.success_url
        return super().get_success_url()


class UserLogoutView(TemplateView):

    template_name = "accounts/logout_page.html"

    def get(self, request: HttpRequest):
        logout(request)
        return redirect('show home')



class ProfileDetailsView(DetailView):
    model = Profile
    template_name = 'accounts/profile_details.html'
    context_object_name = 'profile'


    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['garden'] = 'user'
        gardens = list(Profile.objects.filter(user_id=self.object.user_id))
        plants = list(Profile.objects.filter(user_id=self.object.user_id))

        total_plants_count = len(plants)
        total_gardens_count = len(gardens)

        context.update({
            'garden': 'user',
            'total_plants_count': total_plants_count,
            'total_gardens_count': total_gardens_count,
            'is_owner': self.object.user_id == self.request.user.id,

        })

        return context


class EditProfileView:
    pass


def change_password(request):
    if request.method == 'POST':
        form = PasswordChangeForm(request.user, request.POST)
        if form.is_valid():
            user = form.save()
            update_session_auth_hash(request, user)
            messages.success(request, 'Your password was successfully updated!')
            return redirect('accounts:change_password')
        else:
            messages.error(request, 'Please correct the error below.')
    else:
        form = PasswordChangeForm(request.user)
    return render(request, 'accounts/change_password.html', {
        'form': form
    })