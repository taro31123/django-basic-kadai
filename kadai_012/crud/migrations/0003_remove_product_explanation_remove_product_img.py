# Generated by Django 5.1.3 on 2024-11-23 14:33

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ("crud", "0002_category_product_explanation_product_img_and_more"),
    ]

    operations = [
        migrations.RemoveField(
            model_name="product",
            name="explanation",
        ),
        migrations.RemoveField(
            model_name="product",
            name="img",
        ),
    ]