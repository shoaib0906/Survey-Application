# Generated by Django 3.1.5 on 2021-01-16 07:20

from django.conf import settings
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('question', '0003_answer'),
    ]

    operations = [
        migrations.AlterUniqueTogether(
            name='answer',
            unique_together={('question_id', 'answer_id', 'created_by')},
        ),
    ]
