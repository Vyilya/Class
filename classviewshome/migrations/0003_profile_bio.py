# Generated by Django 5.0b1 on 2023-11-05 10:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('classviewshome', '0002_profile'),
    ]

    operations = [
        migrations.AddField(
            model_name='profile',
            name='bio',
            field=models.TextField(blank=True, null=True),
        ),
    ]
