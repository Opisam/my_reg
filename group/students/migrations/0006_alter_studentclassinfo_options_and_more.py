# Generated by Django 4.0.5 on 2022-06-24 08:15

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('students', '0005_studentclassinfo_class_short_form'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='studentclassinfo',
            options={'verbose_name_plural': 'Class List'},
        ),
        migrations.AlterModelOptions(
            name='studentinfo',
            options={'verbose_name_plural': 'Student List'},
        ),
        migrations.AlterModelOptions(
            name='studentsectioninfo',
            options={'verbose_name_plural': 'Section List'},
        ),
        migrations.AlterModelOptions(
            name='studentshiftinfo',
            options={'verbose_name_plural': 'Shift List'},
        ),
    ]
