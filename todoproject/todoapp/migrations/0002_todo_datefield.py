# Generated by Django 4.1.7 on 2023-02-16 15:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('todoapp', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='todo',
            name='datefield',
            field=models.DateField(default='2222-2-2'),
            preserve_default=False,
        ),
    ]
