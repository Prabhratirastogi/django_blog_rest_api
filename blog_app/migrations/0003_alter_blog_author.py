# Generated by Django 4.2.4 on 2023-08-26 18:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog_app', '0002_blog_is_public'),
    ]

    operations = [
        migrations.AlterField(
            model_name='blog',
            name='author',
            field=models.CharField(max_length=100),
        ),
    ]