from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth import authenticate, login, logout
# Create your views here.
def register_view(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('login')
    else:
        form = UserCreationForm()
    return render(request, 'register.html', {'form': form})

def login_view(request): 
    if request.method == 'POST':
        user_name = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=user_name, password=password)
        if user is not None:
            login(request, user)
            return redirect('cars_list')
        else:
            login_form = AuthenticationForm()
    else:
        login_form = AuthenticationForm()
    return render(request, 'login.html', {'login_form': login_form})

def logout_view(request):
    logout(request)
    return redirect('cars_list')