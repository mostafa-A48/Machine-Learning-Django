# Generated by Django 2.2.6 on 2019-11-26 18:27

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='News',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('headline', models.CharField(max_length=1000)),
                ('predicted_category', models.CharField(max_length=1000)),
            ],
        ),
    ]
