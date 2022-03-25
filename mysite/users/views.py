from django.contrib.auth.models import User
from django.shortcuts import render, HttpResponse, redirect
from django.contrib.auth import authenticate, login
from .forms import LoginForm, RegistrationForm
from django.contrib.auth.backends import ModelBackend
from django.db.models import Q
from .models import EmailVerification
from utils.email_send import send_register_email


class MyBackend(ModelBackend):
    """email login test"""

    def authenticate(self, request, username=None, password=None, **kwargs):
        try:
            user = User.objects.get(Q(username=username) | Q(email=username))
            if user.check_password(password):
                return user
        except Exception as e:
            return None


def activation_user(request, active_code):
    """Compare verification codes and update user status"""
    all_records = EmailVerification.objects.filter(code=active_code)
    if all_records:
        for r in all_records:
            email = r.email
            user = User.objects.get(email=email)
            user.is_staff = True
            user.save()
    else:
        return HttpResponse('Wrong link!')
    return redirect('users:login')


# Create your views here.
def login_view(request):
    if request.method != 'POST':
        form = LoginForm()
    else:
        form = LoginForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            user = authenticate(request, username=username, password=password)
            if user is not None:
                login(request, user)
                # if login is successful, redirect to the certain page
                return redirect('/admin')
            else:
                # login failed
                return HttpResponse("Invalid username or password!")
    context = {'form': form}
    return render(request, 'users/login.html', context)


def register(request):
    """Registration view"""
    if request.method != 'POST':
        form = RegistrationForm()
    else:
        form = RegistrationForm(request.POST)
        if form.is_valid():
            new_user = form.save(commit=False)
            new_user.set_password(form.cleaned_data.get('password'))
            new_user.username = form.cleaned_data.get('email')
            new_user.save()
            send_register_email(form.cleaned_data.get('email'), 'register')
            return HttpResponse('Success!')
    context = {'form': form}
    return render(request, 'users/register.html', context)
