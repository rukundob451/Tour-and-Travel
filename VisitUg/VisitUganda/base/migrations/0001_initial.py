# Generated by Django 4.1.1 on 2022-09-28 06:26

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Company',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('location', models.CharField(max_length=255)),
                ('contact', models.CharField(max_length=255)),
                ('email', models.EmailField(max_length=254)),
                ('account', models.CharField(max_length=255)),
            ],
        ),
        migrations.CreateModel(
            name='Package',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('img', models.ImageField(upload_to='pics')),
                ('company', models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, to='base.company')),
            ],
        ),
        migrations.CreateModel(
            name='Accomodation',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('img', models.ImageField(upload_to='pics')),
                ('package', models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, to='base.package')),
            ],
        ),
    ]