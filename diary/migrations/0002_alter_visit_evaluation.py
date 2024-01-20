# Generated by Django 5.0.1 on 2024-01-18 11:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('diary', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='visit',
            name='evaluation',
            field=models.SmallIntegerField(choices=[(1, 'Bad'), (2, 'Not good'), (3, 'Normal'), (4, 'Good'), (5, 'Very good')], default=1),
        ),
    ]
