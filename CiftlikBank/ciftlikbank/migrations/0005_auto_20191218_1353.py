# Generated by Django 3.0.1 on 2019-12-18 13:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ciftlikbank', '0004_auto_20191218_1347'),
    ]

    operations = [
        migrations.AlterField(
            model_name='sellitem',
            name='image',
            field=models.ImageField(blank=True, null=True, upload_to='media'),
        ),
    ]