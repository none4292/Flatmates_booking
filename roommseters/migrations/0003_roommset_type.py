# Generated by Django 4.1.7 on 2023-02-27 18:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("roommseters", "0002_roommset_lifestaly"),
    ]

    operations = [
        migrations.AddField(
            model_name="roommset",
            name="type",
            field=models.CharField(
                blank=True,
                choices=[("seeker", "seeker"), ("seracher", "seracher")],
                max_length=50,
                null=True,
            ),
        ),
    ]
