# Generated by Django 4.1.7 on 2023-04-23 21:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('school', '0003_alter_school_name'),
    ]

    operations = [
        migrations.AlterField(
            model_name='school',
            name='name',
            field=models.CharField(blank=True, default=None, max_length=50, unique=True),
        ),
    ]
