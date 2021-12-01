# Generated by Django 3.2.5 on 2021-12-01 13:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('projects', '0002_review_tag'),
    ]

    operations = [
        migrations.AddField(
            model_name='project',
            name='tags',
            field=models.ManyToManyField(blank=True, to='projects.Tag'),
        ),
        migrations.AddField(
            model_name='project',
            name='vote_ratio',
            field=models.IntegerField(blank=True, default=0, null=True),
        ),
        migrations.AddField(
            model_name='project',
            name='vote_total',
            field=models.IntegerField(blank=True, default=0, null=True),
        ),
    ]