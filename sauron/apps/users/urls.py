from django.urls import path

from .views import UserDetailView, UserRedirectView, UserUpdateView


app_name = "users"
urlpatterns = [
    path("<uuid:id>/", view=UserDetailView.as_view(), name="detail"),
    path("~update/", view=UserUpdateView.as_view(), name="update"),
    path("~redirect/", view=UserRedirectView.as_view(), name="redirect"),
]
