from django.urls import path
from .views import CustomLoginView, CustomPasswordResetView, CustomPasswordResetDoneView, CustomPasswordResetConfirmView, CustomPasswordResetCompleteView
from django.contrib.auth.views import LogoutView,LoginView
from . import views
from django.contrib.auth import views as auth_view
from .forms import LoginForm,MyPasswordResetForm,MyPasswordChangeForm,MySetPasswordForm


urlpatterns = [
    path('', views.index, name='index'),
    path('login/', LoginView.as_view(template_name='login.html'), name='login'),
  

    path('password-reset/',auth_view.PasswordResetView.as_view(template_name='password_reset.html',form_class=MyPasswordResetForm),name='password_reset'),
    path('password-reset/done/',auth_view.PasswordResetDoneView.as_view(template_name='password_reset_done.html'),name='password_reset_done'),
    path('password-reset-confirm/<uidb64>/<token>/',auth_view.PasswordResetConfirmView.as_view(template_name='password_reset_confirm.html',form_class=MySetPasswordForm),name='password_reset_confirm'),
    path('password-reset-complete/',auth_view.PasswordResetCompleteView.as_view(template_name='password_reset_complete.html'),name='password_reset_complete'),
    path('logout/',views.logout,name='logout'),
    
]
