# Generated by Django 3.2.3 on 2021-05-27 15:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('people', '0002_alter_personproperties_properties'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='personproperties',
            name='properties',
        ),
        migrations.AddField(
            model_name='personproperties',
            name='data',
            field=models.JSONField(null=True),
        ),
    ]