from django.urls import path

from Cottage_garden_project.accounts.views import UserLoginView, UserRegistrationView, ProfileDetailsView, ChangeUserPasswordView

urlpatterns = (
    path('login/', UserLoginView.as_view(), name='login user'),
    path('register/', UserRegistrationView.as_view(), name='register user'),
    path('<int:pk>/', ProfileDetailsView.as_view(), name='profile details'),
    path('edit-password/', ChangeUserPasswordView.as_view(), name='change password'),
)