# Generated by Django 2.2 on 2019-04-12 18:21

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0007_movmensalista'),
    ]

    operations = [
        migrations.AlterField(
            model_name='movmensalista',
            name='veiculo',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='core.Veiculo'),
        ),
    ]
