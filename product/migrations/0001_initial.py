# Generated by Django 4.2.4 on 2023-09-25 02:40

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Product',
            fields=[
                ('product_id', models.IntegerField(max_length=40, primary_key=True, serialize=False, unique=True, verbose_name='상품번호')),
                ('name', models.CharField(max_length=50, verbose_name='상품명')),
                ('price', models.IntegerField(max_length=11, verbose_name='상품가격')),
                ('stock', models.IntegerField(max_length=11, verbose_name='재고')),
                ('cumulative_stock_volume', models.IntegerField(max_length=11, verbose_name='누적 판매량')),
                ('views_count', models.IntegerField(max_length=11, verbose_name='상품 조회수')),
                ('product_register_date', models.DateField(auto_now_add=True)),
                ('product_update_date', models.DateTimeField(auto_now=True)),
            ],
        ),
    ]