# Generated by Django 4.1.1 on 2022-10-02 10:06

import django.core.validators
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Breed',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(default='mixture', max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='Owner',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(default='John Doe', max_length=50)),
                ('age', models.IntegerField()),
            ],
            options={
                'ordering': ['name', 'age'],
            },
        ),
        migrations.CreateModel(
            name='Doggo',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(default='Boglárka', max_length=30, validators=[django.core.validators.MinLengthValidator(1)])),
                ('age', models.IntegerField(default=3, validators=[django.core.validators.MinValueValidator(0), django.core.validators.MaxValueValidator(60)])),
                ('color', models.CharField(default='Black', max_length=20, validators=[django.core.validators.MinLengthValidator(1)])),
                ('isBiting', models.BooleanField(default=False)),
                ('sex', models.CharField(choices=[('M', 'Male'), ('F', 'Female')], default='M', max_length=1)),
                ('breed', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='dog_views.breed')),
                ('owner', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='dog_views.owner')),
            ],
        ),
    ]
