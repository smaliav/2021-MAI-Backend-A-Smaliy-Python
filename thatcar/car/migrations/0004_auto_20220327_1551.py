# Generated by Django 3.2.8 on 2022-03-27 15:51

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('car', '0003_carcolor'),
    ]

    operations = [
        migrations.AlterField(
            model_name='car',
            name='category',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='car.carcategory', verbose_name='Категория'),
        ),
        migrations.AlterField(
            model_name='carbrand',
            name='name',
            field=models.CharField(max_length=32, unique=True, verbose_name='Название'),
        ),
        migrations.AlterField(
            model_name='carcategory',
            name='name',
            field=models.CharField(max_length=32, unique=True, verbose_name='Название'),
        ),
        migrations.AlterField(
            model_name='carcolor',
            name='rgb',
            field=models.CharField(max_length=7, unique=True, verbose_name='Код'),
        ),
    ]
