# Generated by Django 4.0.4 on 2022-04-30 18:34

import ckeditor.fields
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0004_alter_yazi_image_alter_yazi_slug'),
    ]

    operations = [
        migrations.AlterField(
            model_name='yazi',
            name='description',
            field=ckeditor.fields.RichTextField(),
        ),
    ]
