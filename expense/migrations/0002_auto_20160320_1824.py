# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('expense', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='budget',
            name='user',
            field=models.OneToOneField(default=4, to=settings.AUTH_USER_MODEL),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='budget',
            name='budget_amount',
            field=models.DecimalField(max_digits=11, decimal_places=2),
        ),
    ]
