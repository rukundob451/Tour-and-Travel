# Generated by Django 4.1.1 on 2022-09-28 06:59

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='company',
            name='contact',
        ),
        migrations.CreateModel(
            name='Transport',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('img', models.ImageField(upload_to='pics')),
                ('package', models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, to='base.package')),
            ],
        ),
        migrations.CreateModel(
            name='Contact',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('number', models.CharField(max_length=255)),
                ('company', models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, to='base.company')),
            ],
        ),
        migrations.CreateModel(
            name='Activity',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('img', models.ImageField(upload_to='pics')),
                ('package', models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, to='base.package')),
            ],
        ),
    ]