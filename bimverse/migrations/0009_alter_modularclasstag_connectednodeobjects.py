# Generated by Django 4.2.16 on 2024-09-24 01:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('bimverse', '0008_alter_modularclasstag_connectednodeobjects'),
    ]

    operations = [
        migrations.AlterField(
            model_name='modularclasstag',
            name='connectedNodeObjects',
            field=models.ManyToManyField(blank=True, null=True, related_name='modularClassTags', to='bimverse.nodeobject'),
        ),
    ]
