# Generated by Django 5.0.4 on 2024-06-23 15:58

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('TaskApp', '0002_priority_priority_order_task_created_at_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='priority',
            name='priority_order',
        ),
    ]
