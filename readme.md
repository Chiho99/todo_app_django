### 仮想環境をつくる
$ python3 -m venv venv

### 仮想環境を立ち上げる
$ source venv/bin/activate

### Djangoインストール
$ pip install django

### Start Project
$ django-admin startproject todoproject .

### Create App
$ python manage.py startapp todo

### todoproject/settings.py
TEMPLATES = [<br>
        ...<br>
        'DIRS': [BASE_DIR / 'templates'],<br>
        ...<br>
]

### manage.pyと同じ階層にtemplatesディレクトリをつくる
$ mkdir templates

### todoproject/settings.pyにAppを追加
INSTALLED_APPS = [<br>
    ...<br>
    'todo.apps.TodoConfig',<br>
]

### todoproject/urls.pyでurlの繋ぎ込み
from django.contrib import admin<br>
from django.urls import path, include<br>

urlpatterns = [<br>
    path('admin/', admin.site.urls),<br>
    path('', include('todo.urls'))<br>
]

### todoディレクトリにurls.pyをつくる
$ touch urls.py

### todo/urls.pyにadmin追加
from django.contrib import admin<br>
from django.urls import path, include<br>

urlpatterns = [<br>
    path('admin/', admin.site.urls),<br>
]

### サーバ立てる
$ python manage.py runserver

### Migration filesつくる
$ python manage.py makemigrations
<br>or<br>
$ python manage.py makemigrations todo

### データベースへの書き込み(migrate実行、テーブル作成)
$ python manage.py migrate

### superuserを作成
$ python manage.py createsuperuser

### CRUD機能テンプレート
Create : CreateView<br>
Read: ListView, DAtailView<br>
Update: UpdateView<br>
Delete: DeleteView<br>

### CRUD-R ListView
{% %} : 複雑な処理<br>
{{}} : データ<br>

### CRUD-R DetailView
###### パスでPKを指定<br>
urlpatterns = [<br>
    ...<br>
    path('detail/<int:pk>', TodoDetail.as_view())<br>
]

### CRUD-C CreateView
##### パスを指定<br>
urlpatterns = [<br>
    ...<br>
    path('create/', TodoCreate.as_view())<br>
]<br>
##### formタグの中
{% csrf_token %}

### templates(htmlファイルを使い回す)
<img src="templates/img/キャプチャ.PNG" alt="template_image">
