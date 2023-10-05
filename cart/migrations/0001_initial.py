# Generated by Django 4.2.4 on 2023-10-02 12:13

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Cart',
            fields=[
                ('cart_id', models.IntegerField(primary_key=True, serialize=False, unique=True, verbose_name='장바구니 번호')),
                ('user_id', models.CharField(max_length=40, unique=True, verbose_name='사용자 계정')),
                ('redpill_quantity', models.IntegerField(verbose_name='레드필 수량')),
                ('blupill_quantity', models.IntegerField(verbose_name='블루필 수량')),
                ('cart_register_date', models.DateTimeField(auto_now_add=True, verbose_name='장바구니 생성일자')),
                ('cart_update_date', models.DateTimeField(auto_now=True, verbose_name='장바구니 업데이트일자')),
            ],
        ),
    ]