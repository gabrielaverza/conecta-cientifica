# Generated by Django 3.2.23 on 2023-11-23 00:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('projects', '0017_auto_20231122_2127'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='project',
            name='faculty',
        ),
        migrations.AddField(
            model_name='project',
            name='faculty',
            field=models.ManyToManyField(to='projects.Faculty'),
        ),
    ]