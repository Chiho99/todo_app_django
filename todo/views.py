from django.shortcuts import render
from django.views.generic import ListView, DetailView
from .models import TodoModel
# Create your views here.

"""継承クラスCRUD-R(ListView)"""
class TodoList(ListView):
    template_name = 'list.html'
    # データベースファイルの指定
    model = TodoModel

"""継承クラスCRUD-R(DetailView)"""
class TodoDetail(DetailView):
    template_name = 'detail.html'
    model = TodoModel