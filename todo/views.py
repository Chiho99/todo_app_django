from django.shortcuts import render
from django.views.generic import ListView, DetailView, CreateView
from .models import TodoModel
from django.urls import reverse_lazy
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

"""継承クラスCRUD-C(CreateView)"""
class TodoCreate(CreateView):
    template_name = 'create.html'
    model = TodoModel
    fields = ('title', 'memo', 'priority', 'duedate')
    # reverse 引数→urlで呼ばれる
    success_url = reverse_lazy('list')
