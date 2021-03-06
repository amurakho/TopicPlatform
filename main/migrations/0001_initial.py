# Generated by Django 3.1.2 on 2020-10-05 05:45

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Link',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('url', models.URLField()),
                ('title', models.CharField(max_length=500)),
                ('pub_date', models.DateField(blank=True, null=True)),
                ('text', models.TextField()),
                ('scrapped', models.BooleanField(default=False)),
                ('created_at', models.DateField(auto_now=True)),
            ],
        ),
    ]
