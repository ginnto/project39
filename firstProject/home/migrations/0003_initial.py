# Generated by Django 5.0.2 on 2024-03-14 04:37

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('home', '0002_delete_register'),
    ]

    operations = [
        migrations.CreateModel(
            name='register',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200, unique=True)),
                ('subject', models.CharField(max_length=200)),
                ('address', models.TextField()),
                ('age', models.IntegerField()),
                ('img', models.ImageField(upload_to='picture')),
            ],
        ),
    ]
