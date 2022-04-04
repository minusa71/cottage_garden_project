import plant as plant
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


class UserDashboardView(views.ListView):
    model = Garden
    paginate_by = 10



    # template_name = 'main/dashboard.html'

    # def get_queryset(self):
    #     return Garden.objects.all()


    # def get_context_data(self, **kwargs):
    #     context = super().get_context_data(**kwargs)
    #     context['hide_additional_nav_data'] = True
    #     return context


# class profile_details(views.View):
#     model = Profile
#     template_name = 'template name'


class CreatePlantView(views.CreateView):
    template_name = 'main/add_plant.html'
    form_class = CreatePlantForm
    success_url = reverse_lazy('dashboard')

    def get_form_kwargs(self):
        kwargs = super().get_form_kwargs()
        kwargs['user'] = self.request.user
        return kwargs


class EditPlantView(views.UpdateView):
    # all_plants = Plant.objects.all()
    template_name = 'main/plant_edit.html'
    form_class = EditPlantForm

    def get_queryset(self):
        return Plant.objects.all()




class DeletePlantView(views.DeleteView):
    template_name = 'main/plant_delete.html'
    form_class = DeletePlantForm


class CreateGarden(views.CreateView):
    form_class = CreateGardenForm
    template_name = 'main/create_garden.html'
    success_url = reverse_lazy('dashboard')

    def get_form_kwargs(self):
        kwargs = super().get_form_kwargs()
        kwargs['user'] = self.request.user
        return kwargs





