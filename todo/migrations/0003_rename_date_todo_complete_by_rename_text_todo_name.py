# Generated by Django 4.0.10 on 2024-02-03 21:20

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('todo', '0002_todo_date'),
    ]

    operations = [
        migrations.RenameField(
            model_name='todo',
            old_name='date',
            new_name='complete_by',
        ),
        migrations.RenameField(
            model_name='todo',
            old_name='text',
            new_name='name',
        ),
    ]
