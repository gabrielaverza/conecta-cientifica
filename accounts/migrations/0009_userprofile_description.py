# Generated by Django 3.2.23 on 2023-11-28 03:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0008_userprofile_isteacher'),
    ]

    operations = [
        migrations.AddField(
            model_name='userprofile',
            name='description',
            field=models.TextField(blank=True, default=''),
        ),
    ]