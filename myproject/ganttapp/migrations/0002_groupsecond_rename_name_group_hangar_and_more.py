# Generated by Django 5.1.1 on 2024-09-26 21:03

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ganttapp', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='GroupSecond',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('workshop_name', models.CharField(max_length=100)),
            ],
        ),
        migrations.RenameField(
            model_name='group',
            old_name='name',
            new_name='hangar',
        ),
        migrations.RemoveField(
            model_name='event',
            name='status',
        ),
        migrations.AddField(
            model_name='event',
            name='aircraft_type',
            field=models.CharField(max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='event',
            name='tail_number',
            field=models.CharField(max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='group',
            name='location',
            field=models.CharField(max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='event',
            name='title',
            field=models.CharField(max_length=100),
        ),
        migrations.AddField(
            model_name='event',
            name='group_second',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='ganttapp.groupsecond'),
        ),
    ]
