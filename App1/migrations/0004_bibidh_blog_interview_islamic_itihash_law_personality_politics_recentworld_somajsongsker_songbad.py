# Generated by Django 3.0.6 on 2020-05-30 12:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('App1', '0003_auto_20200530_1830'),
    ]

    operations = [
        migrations.CreateModel(
            name='Bibidh',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=150)),
                ('slug', models.CharField(max_length=100)),
                ('body', models.CharField(max_length=20000)),
                ('date', models.DateTimeField(auto_now_add=True)),
                ('image', models.ImageField(default='abc.png', upload_to='Bibidh')),
            ],
        ),
        migrations.CreateModel(
            name='blog',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=150)),
                ('slug', models.CharField(max_length=100)),
                ('body', models.CharField(max_length=20000)),
                ('date', models.DateTimeField(auto_now_add=True)),
                ('image', models.ImageField(default='abc.png', upload_to='Blog')),
            ],
        ),
        migrations.CreateModel(
            name='interview',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=150)),
                ('slug', models.CharField(max_length=100)),
                ('body', models.CharField(max_length=20000)),
                ('date', models.DateTimeField(auto_now_add=True)),
                ('image', models.ImageField(default='abc.png', upload_to='interview')),
            ],
        ),
        migrations.CreateModel(
            name='Islamic',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=150)),
                ('slug', models.CharField(max_length=100)),
                ('body', models.CharField(max_length=20000)),
                ('date', models.DateTimeField(auto_now_add=True)),
                ('image', models.ImageField(default='abc.png', upload_to='Islamic')),
            ],
        ),
        migrations.CreateModel(
            name='itihash',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=150)),
                ('slug', models.CharField(max_length=100)),
                ('body', models.CharField(max_length=20000)),
                ('date', models.DateTimeField(auto_now_add=True)),
                ('image', models.ImageField(default='abc.png', upload_to='itihash')),
            ],
        ),
        migrations.CreateModel(
            name='law',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=150)),
                ('slug', models.CharField(max_length=100)),
                ('body', models.CharField(max_length=20000)),
                ('date', models.DateTimeField(auto_now_add=True)),
                ('image', models.ImageField(default='abc.png', upload_to='law')),
            ],
        ),
        migrations.CreateModel(
            name='Personality',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=150)),
                ('slug', models.CharField(max_length=100)),
                ('body', models.CharField(max_length=20000)),
                ('date', models.DateTimeField(auto_now_add=True)),
                ('image', models.ImageField(default='abc.png', upload_to='Personality')),
            ],
        ),
        migrations.CreateModel(
            name='politics',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=150)),
                ('slug', models.CharField(max_length=100)),
                ('body', models.CharField(max_length=20000)),
                ('date', models.DateTimeField(auto_now_add=True)),
                ('image', models.ImageField(default='abc.png', upload_to='politics')),
            ],
        ),
        migrations.CreateModel(
            name='Recentworld',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=150)),
                ('slug', models.CharField(max_length=100)),
                ('body', models.CharField(max_length=20000)),
                ('date', models.DateTimeField(auto_now_add=True)),
                ('image', models.ImageField(default='abc.png', upload_to='recentworld')),
            ],
        ),
        migrations.CreateModel(
            name='somajsongsker',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=150)),
                ('slug', models.CharField(max_length=100)),
                ('body', models.CharField(max_length=20000)),
                ('date', models.DateTimeField(auto_now_add=True)),
                ('image', models.ImageField(default='abc.png', upload_to='somajsongsker')),
            ],
        ),
        migrations.CreateModel(
            name='songbad',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=150)),
                ('slug', models.CharField(max_length=100)),
                ('body', models.CharField(max_length=20000)),
                ('date', models.DateTimeField(auto_now_add=True)),
                ('image', models.ImageField(default='abc.png', upload_to='songbad')),
            ],
        ),
    ]
