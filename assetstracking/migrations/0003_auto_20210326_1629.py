# Generated by Django 3.1.7 on 2021-03-26 13:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('assetstracking', '0002_borrowing_employee_rfid_tag'),
    ]

    operations = [
        migrations.AlterField(
            model_name='borrowing',
            name='start_date',
            field=models.DateField(auto_now_add=True, null=True),
        ),
    ]
