# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Submission',
            fields=[
                ('problem_id', models.IntegerField(primary_key=True, unique=True, serialize=False, default=0)),
                ('pub_date', models.DateTimeField(verbose_name='Question Solved')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
    ]
