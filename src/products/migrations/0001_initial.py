# Generated by Django 5.0.7 on 2024-08-06 11:00

import django.db.models.deletion
import pgvector.django
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('contenttypes', '0002_remove_content_type_name'),
    ]

    operations = [
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=200)),
                ('content', models.TextField()),
                ('timestamp', models.DateTimeField(auto_now_add=True)),
                ('can_delete', models.BooleanField(default=False, help_text='Use in jupyter notebook')),
            ],
        ),
        migrations.CreateModel(
            name='Embedding',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('embedding', pgvector.django.VectorField(blank=True, dimensions=768, null=True)),
                ('object_id', models.PositiveIntegerField()),
                ('content_type', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='contenttypes.contenttype')),
            ],
        ),
    ]
