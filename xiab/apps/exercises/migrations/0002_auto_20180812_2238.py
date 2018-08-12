# Generated by Django 2.0.8 on 2018-08-12 22:38

from django.db import migrations, models
import wagtail.core.fields


class Migration(migrations.Migration):

    dependencies = [
        ('exercises', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='exercisepagerelatedpages',
            name='page_link',
        ),
        migrations.AddField(
            model_name='exercisepagerelatedpages',
            name='answer',
            field=models.CharField(default='', max_length=255),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='exercisepagerelatedpages',
            name='question',
            field=wagtail.core.fields.RichTextField(default=''),
            preserve_default=False,
        ),
    ]