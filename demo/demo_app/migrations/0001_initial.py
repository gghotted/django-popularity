# Generated by Django 4.1.1 on 2022-09-07 16:39

from django.db import migrations, models
import django_popularity.fields


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Person',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('mid', django_popularity.fields.MIDField(blank=True, max_length=100)),
                ('mid_checked_by_admin', models.BooleanField(default=False)),
            ],
        ),
        migrations.CreateModel(
            name='RegisterPersonMID',
            fields=[
            ],
            options={
                'proxy': True,
                'indexes': [],
                'constraints': [],
            },
            bases=('demo_app.person',),
        ),
    ]