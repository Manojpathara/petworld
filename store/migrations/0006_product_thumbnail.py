# Generated by Django 5.0 on 2024-02-13 16:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0005_product_status'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='thumbnail',
            field=models.ImageField(blank=True, null=True, upload_to='upload/product_images/thumbnail/'),
        ),
    ]
