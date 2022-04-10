from django.urls import path

from Cottage_garden_project.accounts.views import UserLoginView, UserRegistrationView, ProfileDetailsView, \
    ChangeUserPasswordView, UserLogoutView, change_password

urlpatterns = (
    path('login/', UserLoginView.as_view(), name='login user'),
    path('logout/', UserLogoutView.as_view(), name='logout user'),
    path('register/', UserRegistrationView.as_view(), name='register user'),
    path('<int:pk>/', ProfileDetailsView.as_view(), name='profile details'),
    path('edit-password/', change_password, name='change_password'),
)