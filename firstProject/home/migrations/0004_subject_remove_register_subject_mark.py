# Generated by Django 5.0.2 on 2024-03-15 05:03

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0003_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='subject',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('subject', models.CharField(max_length=200)),
            ],
        ),
        migrations.RemoveField(
            model_name='register',
            name='subject',
        ),
        migrations.CreateModel(
            name='mark',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('mark', models.IntegerField()),
                ('stu_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='home.register')),
                ('sub_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='home.subject')),
            ],
        ),
    ]
