# Generated by Django 3.0.3 on 2021-12-04 04:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0009_apidata_genre'),
    ]

    operations = [
        migrations.AddField(
            model_name='apidata',
            name='genreb',
            field=models.CharField(max_length=256, null=True),
        ),
        migrations.AddField(
            model_name='apidata',
            name='genrec',
            field=models.CharField(max_length=256, null=True),
        ),
        migrations.AddField(
            model_name='apidata',
            name='genred',
            field=models.CharField(max_length=256, null=True),
        ),
    ]
