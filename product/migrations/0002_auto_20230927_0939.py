# Generated by Django 3.2 on 2023-09-27 00:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('product', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='cumulative_stock_volume',
            field=models.IntegerField(verbose_name='누적 판매량'),
        ),
        migrations.AlterField(
            model_name='product',
            name='price',
            field=models.IntegerField(verbose_name='상품가격'),
        ),
        migrations.AlterField(
            model_name='product',
            name='product_id',
            field=models.IntegerField(primary_key=True, serialize=False, unique=True, verbose_name='상품번호'),
        ),
        migrations.AlterField(
            model_name='product',
            name='product_register_date',
            field=models.DateTimeField(auto_now_add=True, verbose_name='상품 등록 일자'),
        ),
        migrations.AlterField(
            model_name='product',
            name='product_update_date',
            field=models.DateTimeField(auto_now=True, verbose_name='상품 업데이트 일자'),
        ),
        migrations.AlterField(
            model_name='product',
            name='stock',
            field=models.IntegerField(verbose_name='재고'),
        ),
        migrations.AlterField(
            model_name='product',
            name='views_count',
            field=models.IntegerField(verbose_name='상품 조회수'),
        ),
    ]
