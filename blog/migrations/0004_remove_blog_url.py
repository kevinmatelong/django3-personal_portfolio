# Generated by Django 4.1.7 on 2023-03-14 14:33

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0003_blog_url'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='blog',
            name='url',
        ),
    ]