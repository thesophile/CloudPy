# Generated by Django 3.2.19 on 2024-07-02 17:13

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('manim', '0002_auto_20240702_1700'),
    ]

    operations = [
        migrations.AddField(
            model_name='code',
            name='name',
            field=models.CharField(default=django.utils.timezone.now, max_length=60),
            preserve_default=False,
        ),
    ]