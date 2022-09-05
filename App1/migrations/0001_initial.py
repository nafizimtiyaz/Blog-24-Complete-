# Generated by Django 3.0.6 on 2020-05-23 10:31

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='artical',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=150)),
                ('slug', models.CharField(max_length=100)),
                ('body', models.CharField(max_length=20000)),
                ('date', models.DateTimeField(auto_now_add=True)),
                ('image', models.ImageField(default='abc.png', upload_to='Artical')),
            ],
        ),
    ]
