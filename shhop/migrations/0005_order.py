# Generated by Django 4.1.3 on 2022-12-18 15:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shhop', '0004_rename_pub_date_contact_date'),
    ]

    operations = [
        migrations.CreateModel(
            name='Order',
            fields=[
                ('oder_id', models.AutoField(primary_key=True, serialize=False)),
                ('items_json', models.CharField(max_length=5000)),
                ('name', models.CharField(max_length=90)),
                ('email_id', models.CharField(max_length=111)),
                ('address', models.CharField(max_length=500)),
                ('city', models.CharField(max_length=111)),
                ('state', models.CharField(max_length=111)),
                ('zip_code', models.CharField(max_length=111)),
                ('phone', models.CharField(max_length=50)),
                ('date_of_order', models.DateTimeField(auto_now=True)),
            ],
        ),
    ]