# Generated by Django 4.2.7 on 2023-12-26 09:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('library_app', '0007_alter_books_category'),
    ]

    operations = [
        migrations.AlterField(
            model_name='books',
            name='category',
            field=models.CharField(blank=True, max_length=5, null=True),
        ),
    ]
