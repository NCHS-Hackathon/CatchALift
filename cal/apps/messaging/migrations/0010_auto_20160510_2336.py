# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('messaging', '0009_auto_20160510_2332'),
    ]

    operations = [
        migrations.AlterField(
            model_name='message',
            name='msg_from',
            field=models.CharField(default=b'', max_length=50),
        ),
    ]
