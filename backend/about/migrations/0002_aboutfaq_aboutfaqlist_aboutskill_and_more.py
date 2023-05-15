# Generated by Django 4.2.1 on 2023-05-15 03:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('about', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='AboutFAQ',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(db_index=True, max_length=100)),
                ('description', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='AboutFaqList',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(db_index=True, max_length=100)),
                ('description', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='AboutSkill',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(db_index=True, max_length=100)),
                ('description', models.TextField()),
            ],
        ),
        migrations.RenameModel(
            old_name='about_list',
            new_name='AboutList',
        ),
        migrations.RenameModel(
            old_name='about_skill_list',
            new_name='AboutSkillList',
        ),
        migrations.DeleteModel(
            name='about_faq',
        ),
        migrations.DeleteModel(
            name='about_faq_list',
        ),
        migrations.DeleteModel(
            name='about_skill',
        ),
    ]