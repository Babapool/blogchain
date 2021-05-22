# Generated by Django 3.2.2 on 2021-05-21 16:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0003_postpage'),
    ]

    operations = [
        migrations.CreateModel(
            name='ContactForm',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('email', models.EmailField(max_length=254)),
                ('website', models.URLField()),
                ('message', models.TextField()),
            ],
        ),
    ]
