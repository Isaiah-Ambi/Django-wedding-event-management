# Generated by Django 5.1.3 on 2024-11-29 11:53

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='guest',
            name='status',
            field=models.CharField(choices=[('Yes', 'Yes'), ('No', 'No'), ('Pending', 'Pending')], default='Pending', max_length=10),
        ),
        migrations.AddField(
            model_name='wedding',
            name='guests',
            field=models.ManyToManyField(to='core.guest'),
        ),
        migrations.AlterField(
            model_name='wedding',
            name='venue',
            field=models.ForeignKey(on_delete=django.db.models.deletion.RESTRICT, to='core.venue'),
        ),
        migrations.DeleteModel(
            name='Invitation',
        ),
    ]
