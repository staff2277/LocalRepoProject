# Generated by Django 5.1.6 on 2025-02-14 20:40

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=108)),
                ('description', models.CharField(max_length=300)),
                ('price', models.IntegerField()),
                ('category', models.CharField(max_length=200)),
            ],
        ),
    ]
