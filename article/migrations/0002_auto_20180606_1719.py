# Generated by Django 2.0.6 on 2018-06-06 14:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('article', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='article',
            name='uwords',
            field=models.IntegerField(editable=False),
        ),
    ]
