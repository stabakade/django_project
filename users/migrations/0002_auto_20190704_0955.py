# Generated by Django 2.1.7 on 2019-07-04 04:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='profile',
            name='bio',
            field=models.CharField(default='Write your bio here', max_length=200),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='profile',
            name='interests',
            field=models.CharField(default='Specify your interests', max_length=300),
            preserve_default=False,
        ),
    ]