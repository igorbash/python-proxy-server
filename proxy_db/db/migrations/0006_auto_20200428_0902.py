# Generated by Django 3.0.5 on 2020-04-28 09:02

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('db', '0005_auto_20200427_0817'),
    ]

    operations = [
        migrations.AlterField(
            model_name='cookie',
            name='user_ip',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='cookies', to='db.Client'),
        ),
        migrations.AlterField(
            model_name='credential',
            name='user_ip',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='credentials', to='db.Client'),
        ),
    ]