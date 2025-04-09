from django.shortcuts import render
from django.http import HttpResponse
from django.contrib import messages
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login
from django.contrib.auth import authenticate as authlogout
from .models import CustomUser
from .forms import MyUserCreationForm, LoginForm, MyPasswordResetForm, MySetPasswordForm, MyPasswordChangeForm



# Create your views here.

def index(request):
    return render(request, "index.html")


def custom_login_view(request):
    if request.method == "POST":
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('/')  # Redirect to homepage
        else:
            messages.error(request, "Invalid username or password")

    return render(request, 'login.html')



from django.contrib.auth.views import LoginView, PasswordResetView, PasswordResetDoneView, PasswordResetConfirmView, PasswordResetCompleteView
from django.urls import reverse_lazy

class CustomLoginView(LoginView):
    template_name = 'login.html'

class CustomPasswordResetView(PasswordResetView):
    template_name = 'password_reset.html'
    email_template_name = 'password_reset_email.html'
    success_url = reverse_lazy('password_reset_done')

class CustomPasswordResetDoneView(PasswordResetDoneView):
    template_name = 'password_reset_done.html'

class CustomPasswordResetConfirmView(PasswordResetConfirmView):
    template_name = 'password_reset_confirm.html'
    success_url = reverse_lazy('password_reset_complete')

class CustomPasswordResetCompleteView(PasswordResetCompleteView):
    template_name = 'password_reset_complete.html'

def charity_page(request):
    return render(request, "charity_page.html")

def seller_page(request):
    return render(request, "seller_page.html")

def normal_user_page(request):
    return render(request, "normal_user_page.html")

def registration(request):
    return render(request, "register.html")

# Registration Views
def register_user(request, redirect_page):
    form = MyUserCreationForm()
    if request.method == 'POST':
        form = MyUserCreationForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            user.username = user.email
            user.save()
            login(request, user)
            messages.success(request, 'Registration successful!')
            return redirect(redirect_page)
        else:
            messages.error(request, 'Error occurred during registration. Please check your inputs.')
    return render(request, 'user_reg.html', {'form': form})

def user_reg(request):
    return register_user(request, 'normal_user_page')

def charity_user_reg(request):
    return register_user(request, 'charity_page')

def seller_reg(request):
    return register_user(request, 'seller_page')

# Logout View
def logout(request):
    authlogout(request)
    return redirect('index')
