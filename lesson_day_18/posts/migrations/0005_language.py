# Generated by Django 5.0 on 2024-01-31 07:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('posts', '0004_country'),
    ]

    operations = [
        migrations.CreateModel(
            name='Language',
            fields=[
                ('language_id', models.AutoField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=45)),
                ('last_update', models.DateTimeField()),
            ],
            options={
                'db_table': 'language',
                'managed': False,
            },
        ),
    ]