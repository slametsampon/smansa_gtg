# Generated by Django 3.1 on 2020-10-06 22:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0005_auto_20201006_1238'),
    ]

    operations = [
        migrations.AddField(
            model_name='smansauser',
            name='bio',
            field=models.TextField(help_text='Enter your bio details here.', max_length=400, null=True),
        ),
    ]
