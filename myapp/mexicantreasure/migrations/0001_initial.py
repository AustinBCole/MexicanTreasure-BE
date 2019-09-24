# Generated by Django 2.2.5 on 2019-09-24 20:35

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Player',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('user_uuid', models.IntegerField()),
                ('username', models.CharField(max_length=10000)),
                ('password', models.CharField(max_length=10000)),
                ('has_active_session', models.BooleanField(default=False)),
                ('friends', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='mexicantreasure.Player')),
            ],
        ),
        migrations.CreateModel(
            name='Session',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('session_uuid', models.IntegerField()),
                ('session_status', models.CharField(max_length=10000)),
                ('players', models.ManyToManyField(to='mexicantreasure.Player')),
            ],
        ),
    ]