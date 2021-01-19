from django.shortcuts import render,redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User

def signin_view(response):
    if response.user.is_authenticated:
        return redirect('/allTodo/')
    context= {"Error": False}
    try:
        if response.method == "POST":
            username = response.POST['username']
            password = response.POST['password']
            email = response.POST['email']
            user = User.objects.create_user(username, email, password)
            user.save()
            login(response, user)
            return redirect('/allTodo/')
    except Exception as ex:
        print(ex)
        context["Error"] =True
    return render(response, 'registration/signin.html', context)


def login_view(response):
    context= {"Error": False}
    if response.user.is_authenticated:
        return redirect('/allTodo/')
    if response.method == "POST":
        username = response.POST['username']
        password = response.POST['password']
        user = authenticate(response, username=username, password=password)
        if user is not None:
            login(response, user)
            return redirect('/allTodo/')
        else:
            context["Error"] = True
    return render(response, 'registration/login.html', context)

def logout_view(response):
    logout(response)
    return redirect('/login/')