# Generated by Django 5.0.3 on 2024-04-07 18:53

import ckeditor.fields
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('App', '0008_product_likes'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='description',
            field=ckeditor.fields.RichTextField(blank=True, null=True),
        ),
    ]
