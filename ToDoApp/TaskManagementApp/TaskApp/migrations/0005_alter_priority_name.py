# Generated by Django 5.0.4 on 2024-06-28 16:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('TaskApp', '0004_alter_task_updated_at'),
    ]

    operations = [
        migrations.AlterField(
            model_name='priority',
            name='name',
            field=models.CharField(choices=[('高', 'High'), ('中', 'Medium'), ('低', 'Low')], max_length=50),
        ),
    ]
