# Generated by Django 2.0.6 on 2018-06-06 15:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('article', '0005_remove_article_title'),
    ]

    operations = [
        migrations.AddField(
            model_name='article',
            name='title',
            field=models.CharField(default='Title', max_length=40),
            preserve_default=False,
        ),
    ]
