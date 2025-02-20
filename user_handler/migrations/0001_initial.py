# Generated by Django 3.0.7 on 2020-08-11 21:05

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='USERS',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('user', models.CharField(max_length=50)),
                ('email', models.CharField(max_length=50)),
                ('password', models.CharField(max_length=50)),
                ('phone', models.CharField(max_length=50)),
                ('last_login', models.DateTimeField(default=django.utils.timezone.now)),
                ('otp_validate', models.IntegerField(default=0)),
            ],
        ),
    ]
