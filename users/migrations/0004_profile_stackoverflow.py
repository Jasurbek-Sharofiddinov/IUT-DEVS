# Generated by Django 3.2.5 on 2021-12-07 15:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0003_auto_20211207_1946'),
    ]

    operations = [
        migrations.AddField(
            model_name='profile',
            name='stackoverflow',
            field=models.CharField(blank=True, max_length=200, null=True),
        ),
    ]