# Generated by Django 5.1.2 on 2024-11-01 10:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mylibrary', '0002_category_routinerecord'),
    ]

    operations = [
        migrations.AddField(
            model_name='category',
            name='depth2',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
        migrations.AddField(
            model_name='category',
            name='depth3',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
        migrations.AddField(
            model_name='category',
            name='depth4',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
        migrations.AddField(
            model_name='category',
            name='depth5',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
    ]
