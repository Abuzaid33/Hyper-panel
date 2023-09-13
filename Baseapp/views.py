from django.shortcuts import render,HttpResponse,redirect
from django.contrib.auth.models import User
from django.contrib.auth import authenticate,login,logout
from django.contrib.auth.decorators import login_required



@login_required(login_url='login')
def home_view(request):
    return render(request, 'home.html')

def pages_404_alt(request):
    return render(request, 'pages-404-alt.html')

def pages_404(request):
    return render(request, 'pages-404.html')

def pages_500(request):
    return render(request, 'pages-500.html')

def pages_confirm_mail_2(request):
    return render(request, 'pages-confirm-mail-2.html')

def pages_confirm_mail(request):
    return render(request, 'pages-confirm-mail.html')

def pages_lock_screen_2(request):
    return render(request, 'pages-lock-screen-2.html')

def pages_lock_screen(request):
    return render(request, 'pages-lock-screen.html')

def pages_login(request):
    return render(request, 'pages-login.html')

def pages_logout(request):
    return render(request, 'pages-logout.html')

def pages_maintenance(request):
    return render(request, 'pages-maintenance.html')

def pages_preloader(request):
    return render(request, 'pages-preloader.html')

def pages_recoverpw_2(request):
    return render(request, 'pages-recoverpw-2.html')

def page_recoverpw(request):
    return render(request, 'pages-recoverpw.html')

def pages_register(request):
    return render(request, 'pages-register.html')

def pages_starter(request):
    return render(request, 'pages-starter.html')

def landing(request):
    return render(request, 'landing.html')

def compact_layout(request):
    return render(request, 'layouts-compact.html')

def detached_layout(request):
    return render(request, 'layouts-detached.html')

def full_layout(request):
    return render(request, 'layouts-full.html')

def fullscreen_layout(request):
    return render(request, 'layouts-fullscreen.html')

def horizontal_layout(request):
    return render(request, 'layouts-horizontal.html')

def hover_layout(request):
    return render(request, 'layouts-hover.html')

def icon_layout(request):
    return render(request, 'layouts-icon-view.html')

def signuppage(request):
    if request.method == 'POST':
        username = request.POST.get('fullname')  # Update to 'fullname' from 'username'
        email = request.POST.get('emailaddress')  # Update to 'emailaddress' from 'email'
        password = request.POST.get('password')  # Update to 'password' from 'password1'
        confirm_password = request.POST.get('password-confirm')  # New field for password confirmation

        if password != confirm_password:
            return HttpResponse("Your passwords do not match")
        else:
            # Create a new user
            my_user = User.objects.create_user(username, email, password)
            my_user.save()
            return redirect('login')

    return render(request, 'signup.html')
    
def loginpage(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')

        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('home')  # Redirect to 'home' page upon successful login
        else:
            return HttpResponse("Invalid credentials")

    return render(request, 'login.html')


def logoutpage(request):
    logout(request)  # Logs out the user
    return render(request, 'logout.html')