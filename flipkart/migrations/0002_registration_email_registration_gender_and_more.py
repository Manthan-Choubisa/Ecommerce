# Generated by Django 4.1.7 on 2023-03-31 07:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('flipkart', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='registration',
            name='email',
            field=models.CharField(blank=True, max_length=50, null=True),
        ),
        migrations.AddField(
            model_name='registration',
            name='gender',
            field=models.CharField(blank=True, max_length=50, null=True),
        ),
        migrations.AddField(
            model_name='registration',
            name='mobile',
            field=models.BigIntegerField(default=0),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='registration',
            name='password',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
    ]
