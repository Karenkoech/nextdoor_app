# Generated by Django 3.2.10 on 2022-06-18 19:01

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='NeighbourHood',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Nextdoor_name', models.CharField(max_length=50)),
                ('Nextdoor_location', models.CharField(max_length=60)),
                ('occupants', models.PositiveIntegerField(default=10)),
                ('health_contact', models.CharField(max_length=255)),
                ('police_contact', models.CharField(max_length=255)),
            ],
        ),
    ]