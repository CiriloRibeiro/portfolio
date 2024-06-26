# Generated by Django 4.2.11 on 2024-04-24 23:47

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Post',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateField(auto_now_add=True)),
                ('headline', models.TextField(max_length=100)),
                ('content', models.TextField()),
                ('image', models.ImageField(upload_to='')),
                ('project_link', models.URLField(blank=True)),
            ],
        ),
    ]
