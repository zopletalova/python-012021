# Generated by Django 3.2 on 2021-04-29 17:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('katalog', '0004_auto_20210429_1900'),
    ]

    operations = [
        migrations.RenameField(
            model_name='vypujcka',
            old_name='zakazník',
            new_name='zakaznik',
        ),
        migrations.AddField(
            model_name='vypujcka',
            name='id_cislo',
            field=models.IntegerField(default=1),
            preserve_default=False,
        ),
    ]
