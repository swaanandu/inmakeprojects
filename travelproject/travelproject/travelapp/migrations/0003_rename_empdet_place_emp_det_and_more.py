# Generated by Django 4.1.6 on 2023-02-06 16:07

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('travelapp', '0002_place_empdet_place_empimg_place_empname'),
    ]

    operations = [
        migrations.RenameField(
            model_name='place',
            old_name='empdet',
            new_name='emp_det',
        ),
        migrations.RenameField(
            model_name='place',
            old_name='empimg',
            new_name='emp_img',
        ),
        migrations.RenameField(
            model_name='place',
            old_name='empname',
            new_name='emp_name',
        ),
    ]
