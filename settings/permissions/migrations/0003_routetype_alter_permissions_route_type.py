# Generated by Django 5.0.6 on 2024-10-04 13:18

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('permissions', '0002_alter_permissions_is_visible'),
    ]

    operations = [
        migrations.CreateModel(
            name='RouteType',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
            ],
        ),
        migrations.AlterField(
            model_name='permissions',
            name='route_type',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='permissions.routetype'),
        ),
    ]
