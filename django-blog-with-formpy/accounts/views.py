from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib import auth

# Create your views here.
def signup(req):
    if req.method == 'POST':
        if req.POST['password1'] == req.POST['password2']:
            user = User.objects.create_user(username = req.POST['username'], password = req.POST['password1'])
            auth.login(req, user)
            return redirect('home')
    return render(req, 'signup.html')

def login(req):
    if req.method == 'POST':
        username = req.POST['username']
        password = req.POST['password']
        user = auth.authenticate(req, username = username, password = password)
        if user is not None:
            auth.login(req, user)
            return redirect('home')
        else:
            return render(req, 'login.html', {'error': 'Wrong username or password'})
    else:
        return render(req, 'login.html')
    return render(req, 'login.html')

def logout(req):
    if req.method == 'POST':
        auth.logout(req)
        return redirect('home')
    return render(req, 'login.html')