# Generated by Django 4.1.7 on 2023-04-16 11:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('adm', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='MyFile',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('file', models.FileField(upload_to='uploads/')),
            ],
        ),
    ]
