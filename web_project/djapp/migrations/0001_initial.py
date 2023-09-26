# Generated by Django 4.2.5 on 2023-09-07 09:55

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Image',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(upload_to='media/hellodj/')),
            ],
        ),
        migrations.CreateModel(
            name='Trubi',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100, verbose_name='Тип/название трубы')),
                ('wall', models.CharField(max_length=10, verbose_name='Cтенка (мм)')),
                ('length', models.CharField(max_length=10, verbose_name='Длина (Метры)')),
                ('weight', models.CharField(max_length=10, verbose_name='Вес 1 единицы (в погонных метрах)')),
                ('price', models.CharField(max_length=10, verbose_name='Цена 1 единицы (в погонных метрах)')),
                ('priceT', models.CharField(max_length=25, verbose_name='Цена 1 Тонны (в погонных метрах)')),
            ],
            options={
                'verbose_name': 'трубу в таблицу "Трубы"',
            },
        ),
    ]
