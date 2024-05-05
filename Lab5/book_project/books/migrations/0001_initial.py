# Generated by Django 5.0.4 on 2024-05-05 12:41

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Book',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=200)),
                ('desc', models.TextField()),
                ('rate', models.DecimalField(decimal_places=1, max_digits=3)),
                ('views', models.IntegerField(default=0)),
            ],
        ),
    ]
