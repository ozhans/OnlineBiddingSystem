# Generated by Django 2.2 on 2019-12-19 19:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ciftlikbank', '0018_auto_20191219_1950'),
    ]

    operations = [
        migrations.AlterField(
            model_name='sellitem',
            name='image',
            field=models.ImageField(blank=True, null=True, upload_to='media'),
        ),
    ]