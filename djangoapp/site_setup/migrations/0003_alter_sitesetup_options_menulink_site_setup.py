# Generated by Django 4.2.1 on 2023-05-16 08:29

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('site_setup', '0002_sitesetup'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='sitesetup',
            options={'verbose_name': 'Setup', 'verbose_name_plural': 'Setup'},
        ),
        migrations.AddField(
            model_name='menulink',
            name='site_setup',
            field=models.ForeignKey(blank=True, default=None, null=True, on_delete=django.db.models.deletion.CASCADE, to='site_setup.sitesetup'),
        ),
    ]