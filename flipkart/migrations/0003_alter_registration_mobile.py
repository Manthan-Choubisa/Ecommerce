# Generated by Django 4.1.7 on 2023-04-03 06:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('flipkart', '0002_registration_email_registration_gender_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='registration',
            name='mobile',
            field=models.BigIntegerField(default=0),
        ),
    ]
