# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('clase', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='ClaseAlumno',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('alumno', models.ForeignKey(to=settings.AUTH_USER_MODEL)),
                ('calificacion', models.ForeignKey(to='clase.Calificacion')),
                ('clase', models.ForeignKey(to='clase.Clase')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.RemoveField(
            model_name='clase',
            name='calificaciones',
        ),
    ]
