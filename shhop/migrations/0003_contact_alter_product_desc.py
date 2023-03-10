# Generated by Django 4.1.3 on 2022-11-19 12:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shhop', '0002_product_image_product_category_product_price_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='Contact',
            fields=[
                ('msgid', models.AutoField(primary_key=True, serialize=False)),
                ('name', models.CharField(default='', max_length=50)),
                ('desc', models.CharField(default='', max_length=500)),
                ('email', models.CharField(default='', max_length=50)),
                ('phone', models.CharField(default='', max_length=50)),
                ('pub_date', models.DateField()),
            ],
        ),
        migrations.AlterField(
            model_name='product',
            name='desc',
            field=models.CharField(max_length=5000),
        ),
    ]
