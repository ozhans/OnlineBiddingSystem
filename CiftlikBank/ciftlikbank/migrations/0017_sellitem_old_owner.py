# Generated by Django 3.0 on 2019-12-19 14:56

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('ciftlikbank', '0016_auto_20191219_1319'),
    ]

    operations = [
        migrations.AddField(
            model_name='sellitem',
            name='old_owner',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.DO_NOTHING, related_name='old_owner', to=settings.AUTH_USER_MODEL),
        ),
    ]
