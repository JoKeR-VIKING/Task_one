from django.shortcuts import render, redirect
from account.forms import UserCreateForm, UserLoginForm
from account.models import UserModel
from django.contrib.auth.models import User
from django.contrib import messages
from django.contrib.auth import authenticate
from django.contrib.auth.hashers import make_password

def home(request):
    if 'username' in request.session:
        return redirect('account:dashboard')

    return render(request, 'account/home.html')

def doctorSignup(request):
    if 'username' in request.session:
        return redirect('account:dashboard')

    form = UserCreateForm()

    if request.method == "POST":
        if request.POST.get('password') != request.POST.get('confirm_password'):
            messages.error(request, 'Passwords do not match.')
            return redirect('account:doctor_signup')

        try:
            user = User.objects.create(
                first_name=request.POST.get('first_name'),
                last_name=request.POST.get('last_name'),
                username=request.POST.get('username'),
                email=request.POST.get('email'),
                password=make_password(request.POST.get('password')),
            )
        except:
            messages.error(request, 'User already exists.')
            return redirect('account:doctor_signup')

        address = request.POST.get('address_line_one') + "," + \
                  request.POST.get('city') + "," + \
                  request.POST.get('state') + "," + request.POST.get('pincode')

        user_model = UserModel.objects.create(
            user=user,
            profile_picture=request.FILES.get('profile_picture'),
            address=address,
            is_doctor=True,
        )

        return redirect('account:doctor_signin')

    return render(request, 'account/doctor_signup.html', context={'form': form})

def paitentSignup(request):
    if 'username' in request.session:
        return redirect('account:dashboard')

    form = UserCreateForm()

    if request.method == "POST":
        if request.POST.get('password') != request.POST.get('confirm_password'):
            messages.error(request, 'Passwords do not match.')
            return redirect('account:paitent_signup')

        try:
            user = User.objects.create(
                first_name=request.POST.get('first_name'),
                last_name=request.POST.get('last_name'),
                username=request.POST.get('username'),
                email=request.POST.get('email'),
                password=make_password(request.POST.get('password')),
            )
        except:
            messages.error(request, 'User already exists.')
            return redirect('account:paitent_signup')

        address = request.POST.get('address_line_one') + "," + \
                  request.POST.get('city') + "," + \
                  request.POST.get('state') + "," + request.POST.get('pincode')

        user_model = UserModel.objects.create(
            user=user,
            profile_picture=request.FILES.get('profile_picture'),
            address=address,
            is_doctor=False,
        )

        return redirect('account:paitent_signin')

    return render(request, 'account/paitent_signup.html', context={'form': form})

def doctorSignin(request):
    if 'username' in request.session:
        return redirect('account:dashboard')

    form = UserLoginForm()

    if request.method == "POST":
        username = request.POST.get('username')
        password = request.POST.get('password')

        user = authenticate(username=username, password=password)

        if user:
            request.session['username'] = username
            messages.success(request, 'Logged in successfully!')
            return redirect('account:dashboard')
        else:
            messages.error(request, 'Check your username/password again!')
            return redirect('account:doctor_signin')

    return render(request, 'account/doctor_signin.html', context={'form': form})

def paitentSignin(request):
    if 'username' in request.session:
        return redirect('account:dashboard')

    form = UserLoginForm()

    if request.method == "POST":
        username = request.POST.get('username')
        password = request.POST.get('password')

        user = authenticate(username=username, password=password)

        if user:
            request.session['username'] = username
            messages.success(request, 'Logged in successfully!')
            return redirect('account:dashboard')
        else:
            messages.error(request, 'Check your username/password again!')
            return redirect('account:paitent_signin')

    return render(request, 'account/paitent_signin.html', context={'form': form})

def dashboard(request):
    if 'username' not in request.session:
        return redirect('account:home')

    username = request.session['username']

    user = UserModel.objects.get(user=User.objects.get(username=username))
    return render(request, 'account/dashboard.html', context={'user': user})

def logout(request):
    if 'username' not in request.session:
        return redirect('account:home')

    del request.session['username']
    messages.info(request, 'Logged out successfully!')
    return redirect('account:home')
