# Generated by Django 4.1.7 on 2023-03-16 14:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0003_rename_fathers_name_profile_father_name'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='profile',
            name='upload_img',
        ),
        migrations.AddField(
            model_name='profile',
            name='code_melli',
            field=models.CharField(default=1, max_length=50),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='profile',
            name='phone',
            field=models.CharField(default='1', max_length=50),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='profile',
            name='mobile',
            field=models.CharField(max_length=50),
        ),
        migrations.AlterField(
            model_name='profile',
            name='postal_code',
            field=models.CharField(max_length=50),
        ),
    ]
