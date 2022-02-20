from django.urls import path
from . import views

app_name = "users"  # define a name space, used to differentiate urls among apps

urlpatterns = [
    path("login/", views.login_view, name="login"),
    path("register/", views.register, name='register'),
    path('activate/<code>', views.activation_user, name='activate')
]