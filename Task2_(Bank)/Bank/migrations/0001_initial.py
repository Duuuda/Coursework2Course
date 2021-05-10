# Generated by Django 3.1.6 on 2021-02-14 16:21

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Client',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50, unique=True, verbose_name='Name')),
                ('balance', models.DecimalField(decimal_places=2, default=0, max_digits=20, verbose_name='Money')),
            ],
            options={
                'verbose_name': "Bank's Client",
                'verbose_name_plural': "Bank's Clients",
            },
        ),
    ]