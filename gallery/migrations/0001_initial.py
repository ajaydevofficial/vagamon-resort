# Generated by Django 2.1.4 on 2019-01-31 15:20

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='gallery',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50, null=True)),
                ('image', models.ImageField(blank=True, null=True, upload_to='gallery/')),
            ],
        ),
    ]
