# Generated by Django 2.2 on 2019-04-05 19:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mywebsite', '0002_auto_20190331_0033'),
    ]

    operations = [
        migrations.CreateModel(
            name='Hobby',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=20)),
                ('description', models.TextField()),
            ],
        ),
    ]
