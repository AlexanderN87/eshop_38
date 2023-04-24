# Generated by Django 4.2 on 2023-04-12 13:00

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('category_name', models.CharField(max_length=15)),
                ('reg_date', models.DateTimeField(auto_now=True)),
            ],
        ),
        migrations.CreateModel(
            name='Products',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('product_name', models.CharField(max_length=75)),
                ('product_count', models.IntegerField()),
                ('product_des', models.TextField()),
                ('product_photo', models.ImageField(upload_to='media')),
                ('product_price', models.FloatField()),
                ('product_category', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='store_main.category')),
            ],
        ),
    ]
