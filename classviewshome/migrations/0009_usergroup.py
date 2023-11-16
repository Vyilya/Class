# Generated by Django 4.2.4 on 2023-11-16 15:09

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('auth', '0012_alter_user_first_name_max_length'),
        ('classviewshome', '0008_customuser_profile_pic_customuser_telegram_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='UserGroup',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('full_name', models.CharField(blank=True, max_length=250, null=True, verbose_name='ФИО')),
                ('profile_pic', models.ImageField(blank=True, null=True, upload_to='images/profile/')),
                ('city', models.CharField(blank=True, max_length=250, null=True, verbose_name='Город')),
                ('group', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='auth.group')),
            ],
        ),
    ]