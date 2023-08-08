# Generated by Django 4.2.3 on 2023-07-29 10:35

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import uuid


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('category', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='product',
            fields=[
                ('uid', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now_add=True)),
                ('subCategory', models.CharField(max_length=20)),
                ('productName', models.CharField(max_length=20)),
                ('productDescription', models.TextField(max_length=100)),
                ('productPrice', models.CharField(max_length=10)),
                ('productRatings', models.CharField(max_length=10)),
                ('prod_img_1', models.ImageField(upload_to='media/productImage')),
                ('prod_img_2', models.ImageField(upload_to='media/productImage')),
                ('prod_img_3', models.ImageField(upload_to='media/productImage')),
                ('categoryName', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='category', to='category.category')),
                ('userProduct', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='userProduct', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'abstract': False,
            },
        ),
    ]
