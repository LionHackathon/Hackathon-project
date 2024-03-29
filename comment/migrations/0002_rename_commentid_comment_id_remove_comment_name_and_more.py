# Generated by Django 4.2.4 on 2023-08-18 11:24

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('post', '0001_initial'),
        ('comment', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='comment',
            old_name='commentId',
            new_name='id',
        ),
        migrations.RemoveField(
            model_name='comment',
            name='Name',
        ),
        migrations.RemoveField(
            model_name='comment',
            name='createdTime',
        ),
        migrations.RemoveField(
            model_name='comment',
            name='modifiedTime',
        ),
        migrations.RemoveField(
            model_name='comment',
            name='questionId',
        ),
        migrations.RemoveField(
            model_name='comment',
            name='reply',
        ),
        migrations.RemoveField(
            model_name='comment',
            name='status',
        ),
        migrations.RemoveField(
            model_name='comment',
            name='userId',
        ),
        migrations.AddField(
            model_name='comment',
            name='content',
            field=models.TextField(default='Your Default Value Here'),
        ),
        migrations.AddField(
            model_name='comment',
            name='post',
            field=models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, to='post.post'),
        ),
    ]
