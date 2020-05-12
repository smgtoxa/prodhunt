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
        return render(requests, "users/signup.html")

def login(requests):
    return render(requests, "users/login.html")
# TODO need to add page 
def logout(requests):
    return render(requests, "users/logout.html")