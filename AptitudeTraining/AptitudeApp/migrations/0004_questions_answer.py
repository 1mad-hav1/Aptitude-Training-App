# Generated by Django 2.0 on 2024-10-26 07:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('AptitudeApp', '0003_prediction_result'),
    ]

    operations = [
        migrations.AddField(
            model_name='questions',
            name='answer',
            field=models.CharField(default=1, max_length=50),
            preserve_default=False,
        ),
    ]
