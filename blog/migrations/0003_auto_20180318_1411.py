# Generated by Django 2.0.3 on 2018-03-18 14:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0002_blogpage'),
    ]

    operations = [
        migrations.AddField(
            model_name='blogpage',
            name='author',
            field=models.CharField(default='nithin', max_length=250),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='blogpage',
            name='title_image',
            field=models.ImageField(blank=True, upload_to=''),
        ),
    ]