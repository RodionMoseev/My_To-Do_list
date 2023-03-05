from django.shortcuts import render
from .models import TodoListItem
from django.http import HttpResponseRedirect

# Create your views here.
def todoappView (request):
    return render (request, 'todolist.html')

# Здесь мы возвращаем список 'all_todo_items' как 'all_items' с помощью функции dictionary (Создаем словарь)

def todoappView(request):
    all_todo_items = TodoListItem.objects.all()
    return render(request, 'todolist.html',
    {'all_items':all_todo_items})

# Создание представление для обработки запроса

def addTodoView(request):
    x = request.POST['content']
    new_item = TodoListItem(content = x)
    new_item.save()
    return HttpResponseRedirect('/todoapp/')

# Создаем кнопку удаления ответа

def deleteTodoView(request, i):
    y = TodoListItem.objects.get(id = i)
    y.delete()
    return HttpResponseRedirect('/todoapp/')