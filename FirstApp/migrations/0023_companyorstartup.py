# Generated by Django 3.0.3 on 2020-11-04 13:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('FirstApp', '0022_auto_20201022_1656'),
    ]

    operations = [
        migrations.CreateModel(
            name='CompanyOrStartup',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Nameofcompany', models.CharField(max_length=75)),
                ('Field', models.CharField(choices=[('Software', 'Software'), ('Data Analyst', 'Data Anlayst'), ('other', 'other'), ('Backup', 'Backup'), ('Bank_Po', 'Bank_Po'), ('Linux', 'Linux'), ('Medical', 'Medical'), ('Networking', 'Networking'), ('Storage', 'Storage'), ('Wintel', 'Wintel')], max_length=75)),
                ('Type', models.CharField(choices=[('Company', 'Company'), ('Startup', 'Startup')], max_length=50)),
                ('Size', models.CharField(choices=[('Big', 'Big'), ('Medium', 'Medium'), ('Small', 'Small'), ('Is a startup', 'Is a startup')], max_length=50)),
                ('UrlToCareerPage', models.URLField(max_length=264)),
            ],
        ),
    ]
