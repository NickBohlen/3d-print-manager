# Generated by Django 5.1.4 on 2024-12-14 01:03

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('prints', '0004_stlfile'),
    ]

    operations = [
        migrations.RenameField(
            model_name='printerror',
            old_name='description',
            new_name='error_message',
        ),
        migrations.RemoveField(
            model_name='printerror',
            name='associated_project',
        ),
        migrations.AddField(
            model_name='printerror',
            name='print_job',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='prints.printjob'),
        ),
        migrations.AddField(
            model_name='printerror',
            name='status',
            field=models.CharField(choices=[('Pending', 'Pending'), ('Resolved', 'Resolved'), ('In Progress', 'In Progress')], default='Pending', max_length=20),
        ),
    ]