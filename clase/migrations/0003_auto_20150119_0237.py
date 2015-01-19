# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('clase', '0002_auto_20150119_0143'),
    ]

    operations = [
        migrations.AddField(
            model_name='clasealumno',
            name='comentario',
            field=models.TextField(default=''),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='clasealumno',
            name='calificacion',
            field=models.IntegerField(),
            preserve_default=True,
        ),
        migrations.DeleteModel(
            name='Calificacion',
        ),
        migrations.AlterUniqueTogether(
            name='clasealumno',
            unique_together=set([('alumno', 'clase')]),
        ),
    ]
