# Generated by Django 3.2.10 on 2022-06-20 14:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('neighbour', '0003_business_neighbourhood_post'),
    ]

    operations = [
        migrations.AddField(
            model_name='neighbourhood',
            name='hood_logo',
            field=models.ImageField(default='nextdoor1.jpg', upload_to=''),
        ),
    ]
