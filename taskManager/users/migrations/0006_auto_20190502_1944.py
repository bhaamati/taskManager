# Generated by Django 2.1.7 on 2019-05-02 19:44

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0005_auto_20190502_1942'),
    ]

    operations = [
        migrations.AlterField(
            model_name='task',
            name='proj',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='project_set', to='users.Project'),
        ),
    ]
