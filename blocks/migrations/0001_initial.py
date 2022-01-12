# Generated by Django 3.2.5 on 2022-01-12 06:13

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Project',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('modified', models.DateTimeField(auto_now=True)),
                ('deleted', models.DateTimeField(blank=True, null=True)),
                ('name', models.CharField(max_length=255)),
                ('baseline', models.PositiveIntegerField()),
                ('bonus', models.PositiveIntegerField(default=0)),
                ('rows', models.PositiveIntegerField(default=1)),
                ('active', models.BooleanField(default=True)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'order_with_respect_to': 'user',
            },
        ),
        migrations.CreateModel(
            name='Block',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('start', models.DateTimeField()),
                ('duration', models.DurationField()),
                ('project', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='blocks.project')),
            ],
        ),
        migrations.AddConstraint(
            model_name='project',
            constraint=models.UniqueConstraint(fields=('user', 'name'), name='unique_name'),
        ),
    ]
