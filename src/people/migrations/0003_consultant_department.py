# Generated by Django 4.2.4 on 2023-08-24 15:08

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('departments', '0002_department_icon'),
        ('people', '0002_alter_management_facebook_alter_management_linkedin_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='consultant',
            name='department',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.PROTECT, to='departments.department'),
            preserve_default=False,
        ),
    ]