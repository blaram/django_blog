# Generated by Django 5.0.7 on 2024-07-16 16:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blogs', '0004_alter_blog_status'),
    ]

    operations = [
        migrations.AlterField(
            model_name='blog',
            name='status',
            field=models.TextField(choices=[('Draft', 'Draft'), ('Published', 'Published')], default='Draft', max_length=20),
        ),
    ]
