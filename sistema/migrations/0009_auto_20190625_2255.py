# Generated by Django 2.2.1 on 2019-06-26 02:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('sistema', '0008_auto_20190625_2253'),
    ]

    operations = [
        migrations.AlterField(
            model_name='juego',
            name='foto',
            field=models.ImageField(upload_to='portadas/'),
        ),
    ]
