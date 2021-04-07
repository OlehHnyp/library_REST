# Generated by Django 3.1.1 on 2021-04-06 16:50

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('book', '0002_auto_20210406_1950'),
        ('authentication', '0003_auto_20210406_1950'),
        ('order', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='order',
            name='book',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='book.book'),
        ),
        migrations.AlterField(
            model_name='order',
            name='plated_end_at',
            field=models.DateTimeField(),
        ),
        migrations.AlterField(
            model_name='order',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='authentication.customuser'),
        ),
    ]
