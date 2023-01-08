# Generated by Django 4.1.5 on 2023-01-08 16:03

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('project', '0001_initial'),
        ('organization', '0001_initial'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.AddField(
            model_name='organization',
            name='members',
            field=models.ManyToManyField(related_name='org_members', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='organization',
            name='owners',
            field=models.ManyToManyField(related_name='org_owners', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='organization',
            name='projects',
            field=models.ManyToManyField(related_name='org_projects', to='project.project'),
        ),
    ]
