# Generated by Django 3.1.7 on 2022-06-30 20:11

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Post',
            fields=[
                ('id', models.AutoField(help_text='ID Post', primary_key=True, serialize=False, unique=True, verbose_name='id')),
                ('name', models.CharField(help_text='Name Post', max_length=200, unique=True, verbose_name='title')),
                ('content', models.TextField(help_text='Content Post', verbose_name='content')),
                ('email', models.CharField(help_text='email owner Post', max_length=255, verbose_name='email')),
                ('likes', models.PositiveIntegerField(blank=True, help_text='likes Post', null=True, verbose_name='likes')),
                ('dislikes', models.PositiveIntegerField(blank=True, help_text='dislikes Post', null=True, verbose_name='dislikes')),
            ],
            options={
                'ordering': ['id'],
            },
        ),
    ]
