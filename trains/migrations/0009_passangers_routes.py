# Generated by Django 4.1.3 on 2023-01-14 13:41

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('trains', '0008_remove_passangers_users_passangers_users'),
    ]

    operations = [
        migrations.CreateModel(
            name='passangers_routes',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('route', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='route', to='trains.route')),
                ('users', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='user', to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
