from django.urls import path
from .views import home, RegisterView
from users.views import CustomLoginView
from users.forms import LoginForm
from django.contrib.auth import views as auth_views

app_name = 'users'
urlpatterns = [
    path('', home, name='users-home'),
    path('register/', RegisterView.as_view(), name='users-register'),
    path('login/', CustomLoginView.as_view(redirect_authenticated_user=True, template_name='users/login.html',authentication_form=LoginForm), name='login'),
    path('logout/', auth_views.LogoutView.as_view(template_name='users/logout.html'), name='logout'),
]
