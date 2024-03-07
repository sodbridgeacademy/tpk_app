# Generated by Django 4.0 on 2024-03-02 13:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0003_user_is_staff_alter_user_is_superuser'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='user_type',
            field=models.CharField(choices=[('PUBLIC', 'Public User'), ('ADMIN', 'Admin User')], default='PUBLIC', max_length=10),
        ),
    ]
