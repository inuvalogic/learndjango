# Generated by Django 5.0.6 on 2024-06-28 14:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('webapp', '0003_remove_blog_content'),
    ]

    operations = [
        migrations.AddField(
            model_name='blog',
            name='content',
            field=models.TextField(blank=True, null=True),
        ),
    ]