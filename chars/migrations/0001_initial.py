# Generated by Django 5.1.4 on 2025-01-13 09:37

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Char',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(blank=True, null=True, upload_to='images/')),
                ('name', models.CharField(max_length=100)),
                ('age', models.PositiveIntegerField(blank=True, null=True)),
                ('genre', models.CharField(blank=True, choices=[('Male', 'Male'), ('Female', 'Female'), ('Other', 'Other')], max_length=20, null=True)),
                ('affiliation', models.CharField(blank=True, max_length=100, null=True)),
                ('status', models.CharField(blank=True, choices=[('Alive', 'Alive'), ('Dead', 'Dead'), ('Unknown', 'Unknown')], max_length=50, null=True)),
            ],
        ),
    ]
