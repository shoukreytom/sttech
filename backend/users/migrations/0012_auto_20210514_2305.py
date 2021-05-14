# Generated by Django 3.1.8 on 2021-05-14 21:05

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('contenttypes', '0002_remove_content_type_name'),
        ('users', '0011_auto_20210514_2239'),
    ]

    operations = [
        migrations.AlterField(
            model_name='notification',
            name='content_type',
            field=models.ForeignKey(limit_choices_to=models.Q(models.Q(('app_label', 'users'), ('model', 'follownotification')), models.Q(('app_label', 'users'), ('model', 'votenotification')), _connector='OR'), on_delete=django.db.models.deletion.CASCADE, to='contenttypes.contenttype'),
        ),
    ]
