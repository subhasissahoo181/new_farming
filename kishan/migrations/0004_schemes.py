# Generated by Django 4.0.4 on 2022-07-20 15:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('kishan', '0003_rename_first_name_register_fname_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='Schemes',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('scheme_icon', models.CharField(max_length=50)),
                ('scheme_title', models.CharField(max_length=50)),
                ('scheme_desc', models.TextField()),
            ],
        ),
    ]