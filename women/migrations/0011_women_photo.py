# Generated by Django 5.1.6 on 2025-04-07 17:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('women', '0010_uploadfiles_alter_category_options_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='women',
            name='photo',
            field=models.ImageField(blank=True, default=None, null=True, upload_to='photo/%Y/%m/%d/', verbose_name='Фото'),
        ),
    ]
