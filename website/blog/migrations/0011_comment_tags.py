# Generated by Django 4.2.4 on 2023-09-24 18:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0010_post_tags_alter_tag_name'),
    ]

    operations = [
        migrations.AddField(
            model_name='comment',
            name='tags',
            field=models.ManyToManyField(blank=True, to='blog.tag', verbose_name='Теги'),
        ),
    ]
