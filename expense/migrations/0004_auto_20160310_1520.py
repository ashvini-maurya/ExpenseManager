# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('expense', '0003_auto_20160310_1417'),
    ]

    operations = [
        migrations.AddField(
            model_name='transaction',
            name='category',
            field=models.ForeignKey(default=2, to='expense.Category'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='transaction',
            name='user_id',
            field=models.ForeignKey(default=3, to=settings.AUTH_USER_MODEL),
            preserve_default=False,
        ),
    ]
