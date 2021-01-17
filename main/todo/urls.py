from django.urls import path
from .views import addTodo, deleteTodo, checkTodo, allTodo

urlpatterns = [
    path('addTodo/',addTodo),
    path('deleteTodo/',deleteTodo),
    path('checkTodo/',checkTodo),
    path('allTodo/',allTodo),
]