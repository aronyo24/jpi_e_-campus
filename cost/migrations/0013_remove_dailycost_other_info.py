# Generated by Django 5.0.1 on 2024-04-14 08:02

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('cost', '0012_alter_salary_options_alter_dailycost_cost_amount_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='dailycost',
            name='other_info',
        ),
    ]
