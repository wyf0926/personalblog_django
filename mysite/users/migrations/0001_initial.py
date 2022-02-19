# Generated by Django 3.0.4 on 2022-02-18 17:37

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
            name='UserProfile',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nick_name', models.CharField(blank=True, default='', max_length=23, verbose_name='nickname')),
                ('birthday', models.DateField(blank=True, null=True, verbose_name='birthday')),
                ('gender', models.CharField(choices=[('male', 'Male'), ('female', 'Female'), ('prefer_not_to_say', 'Prefer not to say')], default='male', max_length=20, verbose_name='gender')),
                ('address', models.CharField(blank=True, default='', max_length=100, verbose_name='address')),
                ('image', models.ImageField(default='image/default.png', upload_to='image/%Y/%m', verbose_name='Avatar')),
                ('owner', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='User')),
            ],
        ),
    ]