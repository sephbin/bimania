# Generated by Django 4.2.16 on 2024-09-25 04:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('bimverse', '0011_alter_modularclasstag_name'),
    ]

    operations = [
        migrations.AddField(
            model_name='edgeobject',
            name='project',
            field=models.CharField(default='--none--', max_length=256),
        ),
        migrations.AddField(
            model_name='nodeobject',
            name='project',
            field=models.CharField(default='--none--', max_length=256),
        ),
    ]
