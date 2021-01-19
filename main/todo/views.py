from django.shortcuts import render,redirect
from django.contrib.auth.models import User
from .models import ToDo
from .tools import from_date_To_datetime, filtar_segun_fechas


def addTodo(response):
    try:
        if response.method == "POST":
            if response.POST["title"].strip() == "":
                return redirect('/allTodo/')
            user_id = response.user.id
            user = User.objects.filter(id = user_id).first()
            todo = ToDo(title= response.POST["title"], text =  response.POST["text"], user = user)
            if response.POST["tiempo"] != "":
                todo.timestamp = from_date_To_datetime(response.POST["tiempo"])
            todo.save()
    except Exception as ex:
        print(ex)
    return redirect('/allTodo/')

def deleteTodo(response):
    try:
        if response.method == "POST":
            ToDo_id = list(response.POST.keys())[1]
            todo = ToDo.objects.filter(id = ToDo_id).first()
            todo.delete()
    except Exception as ex:
        print(ex)
    return redirect('/allTodo/')

def checkTodo(response):
    try:
        if response.method == "POST":
            ToDo_id = list(response.POST.keys())[1]
            todo = ToDo.objects.filter(id = int(ToDo_id)).first()
            todo.completed = not (todo.completed)
            todo.save()
    except Exception as ex:
        print(ex)
    return redirect('/allTodo/')

def allTodo(response):
    try:
        if response.method == "GET":
            user_id = response.user.id
            user = User.objects.filter(id = user_id).first()
            Todos = ToDo.objects.filter(user = user).all().values()
            if "title" in response.GET:
                Todos = Todos.filter(title__contains = response.GET["title"])
                Todos = Todos.filter(text__contains = response.GET["text"])
                Todos = filtar_segun_fechas(response.GET,Todos)
            context = {"todos" : list(Todos)}
    except Exception as ex:
        print(ex)
    return render(response, 'todo/index.html', context)