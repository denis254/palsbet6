# Generated by Django 4.0.2 on 2023-04-14 07:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('sport', '0002_auto_20201203_1219'),
    ]

    operations = [
        migrations.AddField(
            model_name='freetipsgame',
            name='score',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='rolltipsgame',
            name='score',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='singlebet',
            name='score',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='viptipsgame',
            name='score',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
    ]