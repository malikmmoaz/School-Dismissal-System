# Generated by Django 4.1.7 on 2023-04-23 22:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('school', '0005_alter_school_user'),
    ]

    operations = [
        migrations.AlterField(
            model_name='school',
            name='name',
            field=models.CharField(blank=True, max_length=50, unique=True),
        ),
    ]
