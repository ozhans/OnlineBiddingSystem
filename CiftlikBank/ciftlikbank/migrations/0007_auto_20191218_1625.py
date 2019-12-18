# Generated by Django 3.0.1 on 2019-12-18 16:25

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('ciftlikbank', '0006_auto_20191218_1359'),
    ]

    operations = [
        migrations.AlterField(
            model_name='sellitem',
            name='owner',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='owner', to=settings.AUTH_USER_MODEL),
        ),
    ]