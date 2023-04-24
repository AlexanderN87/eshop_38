# Generated by Django 4.2 on 2023-04-12 13:46

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('store_main', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Feedback',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('user_id', models.IntegerField()),
                ('feed_text', models.TextField()),
                ('reg_date', models.DateTimeField(auto_now=True)),
            ],
        ),
        migrations.CreateModel(
            name='UserCart',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('user_id', models.IntegerField()),
                ('quantity', models.IntegerField()),
                ('total_for_product', models.FloatField()),
                ('user_product', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='store_main.products')),
            ],
        ),
        migrations.CreateModel(
            name='Sale',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('sale_name', models.CharField(max_length=120)),
                ('sale_start', models.DateField()),
                ('sale_end_date', models.DateField()),
                ('sale_products', models.ManyToManyField(to='store_main.products')),
            ],
        ),
    ]
