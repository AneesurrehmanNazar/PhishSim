# Generated by Django 5.1.7 on 2025-03-14 11:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0004_alter_emailtemplate_created_at'),
    ]

    operations = [
        migrations.RenameField(
            model_name='emailtemplate',
            old_name='envelope_sender_full',
            new_name='envelope_sender_email',
        ),
        migrations.AddField(
            model_name='emailtemplate',
            name='envelope_sender_name',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
    ]
