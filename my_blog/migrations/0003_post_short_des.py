# Generated by Django 3.2.2 on 2021-05-07 11:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('my_blog', '0002_alter_post_options'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='short_des',
            field=models.TextField(default='blof', max_length=300),
            preserve_default=False,
        ),
    ]