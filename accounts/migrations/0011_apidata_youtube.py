# Generated by Django 3.0.3 on 2021-12-13 04:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0010_auto_20211204_1027'),
    ]

    operations = [
        migrations.AddField(
            model_name='apidata',
            name='youtube',
            field=models.CharField(max_length=256, null=True),
        ),
    ]
