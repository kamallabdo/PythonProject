# Generated by Django 2.2.3 on 2019-08-10 18:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0004_auto_20190809_2306'),
    ]

    operations = [
        migrations.AddField(
            model_name='fichier',
            name='picture',
            field=models.ImageField(default=2, upload_to='profile_pics'),
            preserve_default=False,
        ),
    ]
