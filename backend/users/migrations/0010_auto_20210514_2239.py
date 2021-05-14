# Generated by Django 3.1.8 on 2021-05-14 20:39

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('contenttypes', '0002_remove_content_type_name'),
        ('users', '0009_auto_20210514_2232'),
    ]

    operations = [
        migrations.AlterField(
            model_name='notification',
            name='content_type',
            field=models.ForeignKey(limit_choices_to={'model__in': ('vote.*', 'follow.*')}, on_delete=django.db.models.deletion.CASCADE, to='contenttypes.contenttype'),
        ),
    ]
