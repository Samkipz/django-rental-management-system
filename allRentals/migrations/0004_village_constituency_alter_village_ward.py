# Generated by Django 4.1 on 2022-09-17 14:03

from django.db import migrations, models
import django.db.models.deletion
import smart_selects.db_fields


class Migration(migrations.Migration):

    dependencies = [
        ('allRentals', '0003_constituency_alter_rental_ward_alter_village_ward_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='village',
            name='constituency',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='allRentals.constituency'),
        ),
        migrations.AlterField(
            model_name='village',
            name='ward',
            field=smart_selects.db_fields.GroupedForeignKey(group_field='constituency', null=True, on_delete=django.db.models.deletion.CASCADE, to='allRentals.ward'),
        ),
    ]
