# Generated by Django 4.2.7 on 2023-12-26 09:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('library_app', '0008_alter_books_category'),
    ]

    operations = [
        migrations.AlterField(
            model_name='books',
            name='category',
            field=models.CharField(blank=True, choices=[('adv', 'adventure stories'), ('cls', 'classics'), ('crm', 'crime'), ('fairy', 'fairy tales'), ('fts', 'fantasy'), ('hrr', 'horror')], max_length=5, null=True),
        ),
    ]
