# Generated by Django 4.0.7 on 2022-08-30 14:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('scoreboard', '0008_alter_score_created_at'),
    ]

    operations = [
        migrations.AddField(
            model_name='score',
            name='edited_at',
            field=models.DateTimeField(auto_now=True),
        ),
    ]
