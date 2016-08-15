# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0002_raghav_admin_is_staff'),
    ]

    operations = [
        migrations.CreateModel(
            name='User_type_2',
            fields=[
                ('myuser_ptr', models.OneToOneField(serialize=False, auto_created=True, to='accounts.MyUser', parent_link=True, primary_key=True)),
                ('email', models.EmailField(unique=True, max_length=254)),
            ],
            options={
                'abstract': False,
            },
            bases=('accounts.myuser',),
        ),
        migrations.RenameModel(
            old_name='raghav_admin',
            new_name='User_type_1',
        ),
    ]
