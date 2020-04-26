# Generated by Django 3.0.3 on 2020-04-26 08:57

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.CharField(max_length=100, primary_key=True, serialize=False)),
            ],
        ),
        migrations.CreateModel(
            name='Credentials',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('token', models.BinaryField()),
                ('user_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='db.User')),
            ],
        ),
        migrations.CreateModel(
            name='Cookie',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('cookie', models.BinaryField()),
                ('user_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='db.User')),
            ],
        ),
    ]