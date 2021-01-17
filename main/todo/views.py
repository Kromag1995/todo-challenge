from django.shortcuts import render
from django.http import JsonResponse
from django.contrib.auth.models import User
from .models import ToDo

# Create your views here.

def addTodo(response):
    status = 200
    try:
        if response.method == "POST":
            user_id = response.user.id
            user = User.objects.filter(id = user_id).first()
            ToDo = ToDo(title= response.POST.tittle, text =  response.POST.text, user = user)
            ToDo.save()
            data ={
                "message":"ToDo created",
            }
    except Exception as ex:
        status = 404
        data = {"message" : ex}
    return JsonResponse(data, status=status)

def deleteTodo(response):
    status = 200
    try:
        if response.method == "POST":
            ToDo_id = response.POST.ToDo_id
            ToDo = ToDo.objects.filter(id = ToDo_id).first()
            ToDo.delete()
            data ={
                "message":"ToDo deleted",
            }
    except Exception as ex:
        status = 404
        data = {"message" : ex}
    return JsonResponse(data, status=status)

def checkTodo(response):
    status = 200
    try:
        if response.method == "POST":
            ToDo_id = response.POST.ToDo_id
            ToDo = ToDo.objects.filter(id = ToDo_id).first()
            ToDo.completed = not ToDo.completed
            data ={
                "message":"ToDo completed invertido",
            }
    except Exception as ex:
        status = 404
        data = {"message" : ex}
    return JsonResponse(data, status=status)

def allTodo(response):
    status = 200
    try:
        if response.method == "GET":
            user_id = response.user.id
            user = User.objects.filter(id = user_id).first()
            Todos = ToDo.objects.filter(user = user).all().values()
            context = {"todos" : list(Todos)}    
    except Exception as ex:
        status = 404
        data = {"message" : ex}
    return render(response, 'todo/index.html', context)