# Generated by Django 2.1.7 on 2019-03-24 01:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0003_auto_20190322_0746'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='url',
            field=models.TextField(blank=True, help_text='www.website.com', null=True),
        ),
    ]
