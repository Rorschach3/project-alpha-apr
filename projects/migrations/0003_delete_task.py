# Generated by Django 4.1.5 on 2023-01-25 17:28

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ("projects", "0002_task"),
    ]

    operations = [
        migrations.DeleteModel(
            name="Task",
        ),
    ]
