# Generated by Django 4.2.8 on 2024-03-13 13:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='cart',
            name='created_at',
            field=models.DateTimeField(auto_now_add=True, db_column='created_At'),
        ),
        migrations.AlterField(
            model_name='cart',
            name='updated_at',
            field=models.DateTimeField(auto_now_add=True, db_column='updated_At'),
        ),
    ]