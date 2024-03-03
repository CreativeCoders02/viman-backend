# Generated by Django 5.0.1 on 2024-03-03 07:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='testmodel',
            name='image',
        ),
        migrations.RemoveField(
            model_name='testmodel',
            name='message',
        ),
        migrations.AddField(
            model_name='testmodel',
            name='emailId',
            field=models.EmailField(default='creativecoders.vitb@gmail.com', max_length=100),
        ),
    ]
