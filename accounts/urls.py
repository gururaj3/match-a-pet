from django.urls import path
from . import views
from .views import PetListView
from django.contrib.auth import views as auth_views
from .views import VerificationView

app_name = "accounts"
urlpatterns = [
    path("", views.home, name="accounts-home"),
    path("shelter/register/", views.registerShelter, name="register-shelter"),
    path("user/register/", views.registerUser, name="register-user"),
    path(
        "login/",
        auth_views.LoginView.as_view(template_name="accounts/login.html"),
        name="login",
    ),
    path(
        "logout/",
        auth_views.LogoutView.as_view(template_name="accounts/home.html"),
        name="logout",
    ),
    path("shelter/profile/", views.shelterProfile, name="shelter-profile"),
    path("user/profile/", views.clientuserProfile, name="user-profile"),
    path("pets/register/", views.petsRegister, name="pet-register"),
    path("activate/<uidb64>/<token>", VerificationView.as_view(), name="activate"),
    path("view_pets/", PetListView.as_view(), name="view-pets"),
    path("pets/<id>/", views.petProfile, name="pet-profile"),
    path("profile/<username>/", views.shelter_profile, name="shelterprofile"),
    path("favorite/<int:id>/", views.favorite_pet, name="favorite_pet"),
    path("user/favorites", views.favorites_list, name="favorite_list"),
    path("inbox/", views.inbox, name="inbox"),
    path("inbox/<username>", views.Directs, name="directs"),
    path("send/", views.SendDirect, name="send_direct"),
    path("send/new/<username>/", views.NewConversation, name="newconversation"),
]
