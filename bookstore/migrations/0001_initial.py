# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Book',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('title', models.CharField(max_length=255, verbose_name='title')),
                ('publisher', models.CharField(max_length=255, verbose_name='publisher')),
                ('author', models.CharField(max_length=255, verbose_name='author')),
                ('description', models.TextField(verbose_name='description', blank=True)),
                ('coverart', models.ImageField(null=True, upload_to=b'bookstore', blank=True)),
                ('added', models.DateTimeField(default=datetime.datetime.now, verbose_name='added')),
                ('adder', models.ForeignKey(related_name='added_books', verbose_name='adder', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'ordering': ('-added',),
            },
        ),
    ]
