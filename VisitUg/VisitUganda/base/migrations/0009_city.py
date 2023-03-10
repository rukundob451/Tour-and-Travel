# Generated by Django 4.1.1 on 2022-09-29 05:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0008_company_img'),
    ]

    operations = [
        migrations.CreateModel(
            name='City',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('img', models.ImageField(upload_to='pics')),
                ('region', models.CharField(max_length=355)),
                ('description', models.TextField()),
            ],
        ),
    ]
