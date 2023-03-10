# Generated by Django 4.1 on 2023-02-04 20:33

from django.db import migrations, models
import uuid


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Game',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('code', models.UUIDField(default=uuid.UUID('a6054df7-ae7e-4868-8f4f-c7879b074959'))),
                ('player_one', models.CharField(max_length=50)),
                ('player_two', models.CharField(blank=True, max_length=50, null=True)),
                ('start_date', models.DateTimeField(blank=True, null=True)),
                ('end_date', models.DateTimeField(blank=True, null=True)),
            ],
        ),
    ]
