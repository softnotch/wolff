# Generated by Django 2.2.7 on 2019-11-26 00:30

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('contenttypes', '0002_remove_content_type_name'),
        ('accounting', '0004_auto_20191125_1604'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='journalitem',
            name='source_reference',
        ),
        migrations.RemoveField(
            model_name='journalitem',
            name='source_type',
        ),
        migrations.AddField(
            model_name='journalitem',
            name='content_type',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.PROTECT, to='contenttypes.ContentType'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='journalitem',
            name='object_id',
            field=models.CharField(default=1, max_length=200),
            preserve_default=False,
        ),
    ]
