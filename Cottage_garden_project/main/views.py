from django.contrib.auth import forms as auth_forms
from django.urls import reverse_lazy
from django.views import generic as views
from django.shortcuts import render, redirect
from Cottage_garden_project.main.forms import CreateGardenForm,  CreatePlantForm, \
    EditPlantForm, DeletePlantForm
from Cottage_garden_project.main.models import Profile, Plant, Garden


class HomeView(views.TemplateView):
    template_name = 'main/home_page.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['hide_additional_nav_data'] = True
        return context

    # def dispatch(self, request, *args, **kwargs):
    #     if request.user.is_authenticated:
    #         return redirect('dashboard')
    #     return super().dispatch(request,args,kwargs)


class DashboardView(views.ListView):
    model = Garden
    template_name = 'main/dashboard.html'
    context_object_name = Garden.objects.all()

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['hide_additional_nav_data'] = True
        return context


class profile_details(views.View):
    model = Profile
    template_name = 'template name'


def show_dashboard(request):
    return render(request, 'main/dashboard.html')


class UserDashboardView(views.ListView):
    def show_dashboard(self):
        return render(self, 'main/dashboard.html')


class CreatePlantView(views.CreateView):
    template_name = 'main/add_plant.html'
    form_class = CreatePlantForm

    def get_form_kwargs(self):
        kwargs = super().get_form_kwargs()
        kwargs['user'] = self.request.user
        return kwargs


class EditPlantView(views.UpdateView):
    template_name = 'main/plant_edit.html'
    form_class = EditPlantForm


class DeletePlantView(views.DeleteView):
    template_name = 'main/plant_delete.html'
    form_class = DeletePlantForm


class CreateGarden(views.CreateView):
    form_class = CreateGardenForm
    template_name = 'main/create_garden.html'

    def get_form_kwargs(self):
        kwargs = super().get_form_kwargs()
        kwargs['user'] = self.request.user
        return kwargs





