# Generated by Django 4.2.4 on 2023-11-22 22:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("projects", "0014_alter_faculty_name"),
    ]

    operations = [
        migrations.AddField(
            model_name="faculty",
            name="sigla",
            field=models.CharField(default="", max_length=20, unique=True),
        ),
    ]