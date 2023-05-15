# Generated by Django 4.2.1 on 2023-05-15 04:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('portfolio', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='PortfolioItemList',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(db_index=True, max_length=50)),
                ('description', models.TextField()),
                ('img_url', models.CharField(max_length=50)),
                ('type', models.CharField(db_index=True, max_length=50)),
            ],
        ),
        migrations.DeleteModel(
            name='portfolio_item_list',
        ),
    ]