# Generated by Django 4.2.3 on 2023-07-25 02:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('archivos', '0002_alter_archivo_archivo'),
    ]

    operations = [
        migrations.AlterField(
            model_name='archivo',
            name='archivo',
            field=models.FileField(upload_to='media/'),
        ),
    ]
