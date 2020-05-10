# Generated by Django 2.2.12 on 2020-05-08 10:25

from django.db import migrations, models
import django.db.models.deletion
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ('wagtail_localize', '0006_delete_language_model'),
        ('newsletter', '0004_localize_2'),
    ]

    operations = [
        migrations.AlterField(
            model_name='newsletterindexpage',
            name='locale',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='+', to='wagtail_localize.Locale'),
        ),
        migrations.AlterField(
            model_name='newsletterindexpage',
            name='translation_key',
            field=models.UUIDField(default=uuid.uuid4, editable=False),
        ),
        migrations.AlterField(
            model_name='newsletterpage',
            name='locale',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='+', to='wagtail_localize.Locale'),
        ),
        migrations.AlterField(
            model_name='newsletterpage',
            name='translation_key',
            field=models.UUIDField(default=uuid.uuid4, editable=False),
        ),
        migrations.AlterUniqueTogether(
            name='newsletterindexpage',
            unique_together={('translation_key', 'locale')},
        ),
        migrations.AlterUniqueTogether(
            name='newsletterpage',
            unique_together={('translation_key', 'locale')},
        ),
    ]