# Generated by Django 4.2.8 on 2024-08-05 14:02

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('password', models.CharField(max_length=128, verbose_name='password')),
                ('last_login', models.DateTimeField(blank=True, null=True, verbose_name='last login')),
                ('is_superuser', models.BooleanField(default=False, help_text='Designates that this user has all permissions without explicitly assigning them.', verbose_name='superuser status')),
                ('first_name', models.CharField(blank=True, max_length=150, verbose_name='first name')),
                ('last_name', models.CharField(blank=True, max_length=150, verbose_name='last name')),
                ('is_staff', models.BooleanField(default=False, help_text='Designates whether the user can log into this admin site.', verbose_name='staff status')),
                ('is_active', models.BooleanField(default=True, help_text='Designates whether this user should be treated as active. Unselect this instead of deleting accounts.', verbose_name='active')),
                ('date_joined', models.DateTimeField(default=django.utils.timezone.now, verbose_name='date joined')),
                ('email', models.EmailField(max_length=255, unique=True)),
                ('full_name', models.CharField(max_length=255)),
                ('otp', models.CharField(blank=True, max_length=6, null=True)),
                ('otp_verified', models.BooleanField(default=False)),
                ('created_at', models.DateTimeField(auto_now=True)),
                ('updated_at', models.DateTimeField(auto_now_add=True)),
            ],
            options={
                'verbose_name': 'user',
                'verbose_name_plural': 'users',
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Complaint',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('complaint_text', models.TextField(blank=True, null=True)),
                ('status', models.CharField(blank=True, max_length=225, null=True)),
                ('created_at', models.DateTimeField(auto_now=True)),
                ('updated_at', models.DateTimeField(auto_now_add=True)),
            ],
            options={
                'db_table': 'complaint',
            },
        ),
        migrations.CreateModel(
            name='ComplaintComment',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('comment', models.TextField(blank=True, null=True)),
                ('created_at', models.DateTimeField(auto_now=True)),
                ('updated_at', models.DateTimeField(auto_now_add=True)),
            ],
            options={
                'db_table': 'complaint_comment',
            },
        ),
        migrations.CreateModel(
            name='Coupon',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('limit', models.IntegerField(blank=True, null=True)),
                ('percentage', models.DecimalField(blank=True, decimal_places=2, max_digits=10, null=True)),
                ('coupon_code', models.CharField(blank=True, max_length=20, null=True)),
                ('expiry_date', models.DateTimeField(blank=True, null=True)),
            ],
            options={
                'db_table': 'coupon',
            },
        ),
        migrations.CreateModel(
            name='Favourite',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
            ],
            options={
                'db_table': 'favourite',
            },
        ),
        migrations.CreateModel(
            name='Images',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('url', models.CharField(blank=True, max_length=255, null=True)),
            ],
            options={
                'db_table': 'images',
            },
        ),
        migrations.CreateModel(
            name='NotificationConfirmation',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('mail_id', models.IntegerField(blank=True, null=True)),
                ('status', models.TextField(blank=True, null=True)),
            ],
            options={
                'db_table': 'notification_confirmation',
            },
        ),
        migrations.CreateModel(
            name='NotificationSetting',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('email_summary', models.BooleanField(blank=True, null=True)),
                ('special_offers', models.BooleanField(blank=True, null=True)),
                ('community_update', models.BooleanField(blank=True, null=True)),
                ('follow_update', models.BooleanField(blank=True, null=True)),
                ('new_messages', models.BooleanField(blank=True, null=True)),
            ],
            options={
                'db_table': 'notification_setting',
            },
        ),
        migrations.CreateModel(
            name='Order',
            fields=[
                ('id', models.UUIDField(primary_key=True, serialize=False)),
                ('vat', models.DecimalField(db_column='VAT', decimal_places=2, max_digits=10, null=True)),
                ('discount', models.DecimalField(decimal_places=2, max_digits=10, null=True)),
                ('status', models.TextField()),
                ('created_at', models.DateTimeField(auto_now=True)),
                ('updated_at', models.DateTimeField(auto_now_add=True)),
                ('subtotal', models.DecimalField(blank=True, decimal_places=2, max_digits=10, null=True)),
                ('payment_status', models.CharField(choices=[('P', 'pending'), ('C', 'complete'), ('F', 'failed')], default='P', max_length=50)),
            ],
            options={
                'db_table': 'order',
            },
        ),
        migrations.CreateModel(
            name='OrderItems',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now=True)),
                ('updated_at', models.DateTimeField(auto_now_add=True)),
                ('deleted_at', models.DateTimeField(blank=True, db_column='deleted_At', null=True)),
                ('is_delete', models.BooleanField(blank=True, null=True)),
                ('status', models.TextField(blank=True, null=True)),
            ],
            options={
                'db_table': 'order_items',
            },
        ),
        migrations.CreateModel(
            name='Payment',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('amount', models.DecimalField(decimal_places=2, max_digits=10)),
                ('description', models.CharField(max_length=50)),
                ('paid', models.BooleanField(default=False)),
            ],
            options={
                'db_table': 'payment',
            },
        ),
        migrations.CreateModel(
            name='ProductCategory',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(blank=True, max_length=300, null=True)),
                ('created_at', models.DateTimeField(auto_now=True)),
                ('updated_at', models.DateTimeField(default=django.utils.timezone.now)),
            ],
            options={
                'db_table': 'product_category',
            },
        ),
        migrations.CreateModel(
            name='ProductReview',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('comment', models.TextField(blank=True, null=True)),
                ('created_at', models.DateTimeField(auto_now=True)),
                ('updated_at', models.DateTimeField(auto_now_add=True)),
            ],
            options={
                'db_table': 'product_review',
            },
        ),
        migrations.CreateModel(
            name='ProductSubCategory',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(blank=True, max_length=300, null=True)),
                ('created_at', models.DateTimeField(auto_now=True)),
                ('updated_at', models.DateTimeField(auto_now_add=True)),
            ],
            options={
                'db_table': 'product_sub_category',
            },
        ),
        migrations.CreateModel(
            name='PromoProduct',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now=True)),
                ('updated_at', models.DateTimeField(auto_now_add=True)),
            ],
            options={
                'db_table': 'promo_product',
            },
        ),
        migrations.CreateModel(
            name='Promotion',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('code', models.CharField(max_length=255)),
                ('promotion_type', models.CharField(max_length=255)),
                ('discount_type', models.TextField(blank=True, null=True)),
                ('quantity', models.BigIntegerField()),
                ('amount', models.DecimalField(decimal_places=2, max_digits=10)),
                ('valid_from', models.DateTimeField()),
                ('valid_to', models.DateTimeField()),
                ('maximum_discount_price', models.DecimalField(blank=True, decimal_places=2, max_digits=10, null=True)),
                ('created_at', models.DateTimeField(auto_now=True)),
                ('updated_at', models.DateTimeField(auto_now_add=True)),
            ],
            options={
                'db_table': 'promotion',
            },
        ),
        migrations.CreateModel(
            name='UserProductRating',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('user_id', models.UUIDField(blank=True, null=True)),
                ('product_id', models.UUIDField(blank=True, null=True)),
                ('rating', models.IntegerField(blank=True, null=True)),
            ],
            options={
                'db_table': 'user_product_rating',
            },
        ),
    ]
