from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib import auth

def signup(requests):
    if requests.method == "POST":
        if requests.POST["password1"] == requests.POST["password2"]:
            try:
                user = User.objects.get(username=requests.POST['username'])
                return render(requests, "users/signup.html", {'error':'username has already been taken'})
            except User.DoesNotExist:
                user = User.objects.create_user(requests.POST["username"], password = requests.POST["password1"])
                auth.login(requests,user)
                return redirect("home")
        else:
            return render(requests, "users/signup.html", {'error':"Passwords doesn't match"})

    else:
        return render(requests, "users/signup.html")

def login(requests):
    if requests.method == 'POST':
        user = auth.authenticate(username=requests.POST["username"], password=requests.POST["password"])
        if user is not None:
            auth.login(requests, user)
            return redirect('home')
        else:
            return render(requests, "users/login.html", {'error':'Username or password is invalid!'})
    else:
        return render(requests, "users/login.html")
    
# TODO need to add page 
def logout(requests):
    if requests.method == 'POST':
        auth.logout(requests)
        return redirect('home')
