from django.urls import path

from Cottage_garden_project.accounts.views import UserRegistrationView, UserLoginView
from Cottage_garden_project.main.views import HomeView, UserDashboardView, CreateGarden, EditPlantView, \
      DeletePlantView, CreatePlantView

urlpatterns = [
      path('', HomeView.as_view(), name='show home'),
      path('dashboard', UserDashboardView.as_view(), name='dashboard'),


      path('create_garden/', CreateGarden.as_view(), name='add garden'),
      path('plant/add/', CreatePlantView.as_view(), name='add plant'),
      path('plant/edit/<int:pk>/', EditPlantView.as_view(), name='edit plant'),
      path('plant/delete/<int:pk>/', DeletePlantView.as_view(), name='delete plant'),


]