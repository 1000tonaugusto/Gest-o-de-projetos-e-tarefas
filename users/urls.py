from django.urls import path
from . import views
from django.contrib.auth import views as auth_views


urlpatterns = [
    path('register', views.registration, name='register'),
    path('logar', views.UserLoginView.as_view(), name='logar'),
    path('logout', views.logout_user, name='logout'),
    path('update-profile', views.update_profile, name='update-profile'),
    path('reset_password', auth_views.PasswordResetView.as_view(template_name='users/password_reset.html'), name='password-reset'),
    path('password_reset/done/', auth_views.PasswordResetDoneView.as_view(template_name='users/password_reset_done.html'), name='password_reset_done'),
    path('reset/<uidb64>/<token>', auth_views.PasswordResetConfirmView.as_view(template_name='users/password_reset_form.html'), name='password_reset_confirm'),
]