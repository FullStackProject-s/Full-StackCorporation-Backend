# Generated by Django 4.1.5 on 2023-01-08 17:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('employee', '0002_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='developer',
            name='specialty',
            field=models.ManyToManyField(blank=True, null=True, to='employee.developerorganizationspecialty'),
        ),
    ]
