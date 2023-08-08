# Generated by Django 4.2.3 on 2023-07-26 12:30

from django.db import migrations, models
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ('authentications', '0003_profile_delete_users'),
    ]

    operations = [
        migrations.CreateModel(
            name='users',
            fields=[
                ('uid', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now_add=True)),
                ('Name', models.CharField(max_length=100)),
                ('Email', models.EmailField(max_length=20, unique=True)),
                ('password', models.CharField(max_length=20)),
            ],
            options={
                'abstract': False,
            },
        ),
    ]
