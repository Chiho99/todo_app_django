from django.shortcuts import render
from django.views.generic.list import ListView
from .models import TodoModel
# Create your views here.

"""継承クラスCRUD-R(ListView)"""
class TodoList(ListView):
    template_name = 'list.html'
    # データベースファイルの指定
    model = TodoModel