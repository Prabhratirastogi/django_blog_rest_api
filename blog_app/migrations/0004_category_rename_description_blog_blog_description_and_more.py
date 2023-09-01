# Generated by Django 4.2.4 on 2023-09-01 02:23

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('blog_app', '0003_alter_blog_author'),
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('category_name', models.CharField(max_length=50)),
            ],
        ),
        migrations.RenameField(
            model_name='blog',
            old_name='description',
            new_name='blog_description',
        ),
        migrations.RenameField(
            model_name='blog',
            old_name='name',
            new_name='blog_title',
        ),
        migrations.AddField(
            model_name='blog',
            name='category',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='category', to='blog_app.category'),
        ),
    ]
