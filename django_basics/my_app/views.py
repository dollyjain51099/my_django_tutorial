from django.shortcuts import render, redirect
from .models import Posts
from .forms import NameForm, CreateUser
from django.contrib.auth import authenticate, login as auth_login, logout as auth_logout
from django.contrib import messages
from django.contrib.auth.decorators import login_required

# Create your views here.
@login_required(login_url='login')
def index(request):
    value = Posts.objects.all()
    form = NameForm()
    if request.method == 'POST':
        form = NameForm(request.POST)
        if form.is_valid():
            form.save()        
    return render(request, 'my_app/index.html', {'form': form, 'value': value})

def register(request):
    if request.method == 'POST':
        form = CreateUser(data=request.POST)
        if form.is_valid():
            form.save()
            return redirect('login')

    else:
        form = CreateUser()
    return render(request, 'accounts/register.html', {'form': form})

def login(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
            
# Check whether the username and password are valid or not
        user = authenticate(request, username=username, password=password)

        if user is not None:
            auth_login(request, user)
            return redirect('index')

        else:
            messages.error(request, "Username or password is incorrect")
    return render(request, 'accounts/login.html')

def logout(request):
    auth_logout(request)
    return redirect('login')


            
