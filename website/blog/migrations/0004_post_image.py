# Generated by Django 4.2.4 on 2023-09-13 17:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0003_remove_post_comments_post_comments'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='image',
            field=models.URLField(default='http://placehold.it/900x300'),
        ),
    ]
