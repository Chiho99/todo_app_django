# Generated by Django 3.1.4 on 2020-12-10 14:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('todo', '0002_auto_20201210_0937'),
    ]

    operations = [
        migrations.AlterField(
            model_name='todomodel',
            name='priority',
            field=models.CharField(choices=[('danger', 'high'), ('secondary', 'nomal'), ('primary', 'low')], max_length=50),
        ),
    ]
