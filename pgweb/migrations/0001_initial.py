# Generated by Django 3.0.5 on 2021-11-25 13:08

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Advertisement',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('aid', models.CharField(max_length=150)),
                ('sub', models.CharField(max_length=150)),
                ('text', models.CharField(max_length=500)),
                ('username', models.CharField(max_length=500)),
                ('datetime', models.CharField(max_length=1000)),
                ('link', models.CharField(max_length=1000)),
            ],
        ),
        migrations.CreateModel(
            name='Blog',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('bid', models.CharField(max_length=150)),
                ('sub', models.CharField(max_length=150)),
                ('text', models.CharField(max_length=500)),
                ('username', models.CharField(max_length=500)),
                ('datetime', models.CharField(max_length=1000)),
            ],
        ),
        migrations.CreateModel(
            name='Contact',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=150)),
                ('email', models.EmailField(max_length=254)),
                ('type', models.CharField(max_length=500)),
                ('sub', models.CharField(max_length=500)),
                ('msg', models.CharField(max_length=1000)),
            ],
        ),
        migrations.CreateModel(
            name='Newsletter',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('email', models.CharField(max_length=200)),
            ],
        ),
        migrations.CreateModel(
            name='UserProfile',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('usernames', models.CharField(max_length=200)),
                ('phoneno', models.CharField(max_length=150)),
                ('pemail', models.EmailField(max_length=254)),
                ('address', models.CharField(max_length=500)),
                ('city', models.CharField(max_length=500)),
                ('taluka', models.CharField(max_length=500)),
                ('district', models.CharField(max_length=500)),
                ('state', models.CharField(max_length=500)),
                ('pincode', models.CharField(max_length=500)),
                ('dob', models.CharField(max_length=500)),
                ('desc', models.CharField(max_length=1000)),
                ('password', models.CharField(max_length=1000)),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
