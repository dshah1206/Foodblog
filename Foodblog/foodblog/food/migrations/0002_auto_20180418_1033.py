# Generated by Django 2.0.3 on 2018-04-18 05:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('food', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='email',
            field=models.EmailField(blank=True, max_length=70, null=True),
        ),
    ]
