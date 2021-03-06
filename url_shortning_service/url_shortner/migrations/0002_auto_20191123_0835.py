# Generated by Django 2.2.7 on 2019-11-23 08:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('url_shortner', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Urls',
            fields=[
                ('short_id', models.SlugField(max_length=6, primary_key=True, serialize=False)),
                ('httpurl', models.URLField()),
                ('pub_date', models.DateTimeField(auto_now=True)),
                ('count', models.IntegerField(default=0)),
            ],
        ),
        migrations.DeleteModel(
            name='Link',
        ),
    ]
