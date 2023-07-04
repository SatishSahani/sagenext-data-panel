from django.shortcuts import redirect, render
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import authenticate, login
from django.contrib.auth import logout
from django.contrib.auth.models import User

from gadwords.models import AdwordData


# Create your views here.
# def login(request):
#     return render(request, 'login.html')

# def dashboard(request):
#     return render(request, 'dashboard.html')


# def login_view(request):
#     if request.method == 'POST':
#         form = AuthenticationForm(request, data=request.POST)
#         if form.is_valid():
#             username = form.cleaned_data.get('username')
#             password = form.cleaned_data.get('password')
#             user = authenticate(username=username, password=password)
#             if user is not None:
#                 login(request, user)
#                 return redirect('dashboard')
#     else:
#         form = AuthenticationForm()
#     return render(request, 'login.html', {'form': form})


def ad_data_list(request):
    ad_data = AdwordData.objects.all()
    return render(request, 'list.html', {'ad_data': ad_data})

from django.shortcuts import render, redirect

from django.shortcuts import render, redirect
from django.contrib import messages

# def login_view(request):
#     if request.method == 'POST':
#         # Retrieve form data
#         email = request.POST.get('Email')
#         password = request.POST.get('password')
        
#         # Perform authentication logic here (e.g., verify email and password)
#         if email == 'brijesh@gmail.com' and password == 'Bri@2022':
#             # Authentication successful
#             # You can store the user's authentication state in the session or a cookie
            
#             return redirect('dashboard')
#         else:
#             # Authentication failed
#             messages.error(request, 'Invalid email or password')
    
#     return render(request, 'login.html')


# def dashboard_view(request):
#     # Add any necessary logic to fetch data or perform operations for the Dashboard page
#     # ...
#     user = request.user
#     return render(request, 'dashboard.html') 

def logout_view(request):
    logout(request)
    return redirect('login')

def login_view(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')

        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('dashboard')
        else:
            message = 'Invalid username or password'
            return render(request, 'login.html', {'message': message})
    else:
        return render(request, 'login.html')

def dashboard_view(request):
    if request.user.is_authenticated:
        # User is authenticated, display the dashboard
        return render(request, 'dashboard.html')
    else:
        # User is not authenticated, redirect to the login page
        return redirect('login')
    

    