# Generated by Django 4.2.8 on 2024-08-06 14:58

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0002_alter_product_category_alter_product_sub_category'),
        ('accounts', '0002_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='productcategory',
            name='user',
        ),
        migrations.RemoveField(
            model_name='productreview',
            name='product',
        ),
        migrations.RemoveField(
            model_name='productreview',
            name='reply',
        ),
        migrations.RemoveField(
            model_name='productreview',
            name='user',
        ),
        migrations.RemoveField(
            model_name='productsubcategory',
            name='parent_category',
        ),
        migrations.DeleteModel(
            name='Payment',
        ),
        migrations.DeleteModel(
            name='ProductCategory',
        ),
        migrations.DeleteModel(
            name='ProductReview',
        ),
        migrations.DeleteModel(
            name='ProductSubCategory',
        ),
    ]
