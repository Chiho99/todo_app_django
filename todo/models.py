from django.db import models

# Create your models here.
class TodoModel(models.Model):
    title = models.CharField(max_length=100)
    memo = models.TextField()

# オブジェクトが生成されると、実行される
    def __str__(self):
        return self.title