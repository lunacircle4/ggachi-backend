# Generated by Django 2.2.4 on 2019-10-27 14:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('letter', '0002_letter_template'),
    ]

    operations = [
        migrations.AddField(
            model_name='letter',
            name='date',
            field=models.DateField(default='1000-10-01'),
            preserve_default=False,
        ),
    ]
