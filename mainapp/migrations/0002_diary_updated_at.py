# Generated by Django 5.0.6 on 2024-06-13 11:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mainapp', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='diary',
            name='updated_at',
            field=models.DateTimeField(auto_now=True),
        ),
    ]
