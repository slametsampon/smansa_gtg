# Generated by Django 3.1 on 2020-10-03 04:11

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(blank=True, choices=[('Pending', 'Pending'), ('Finish', 'Finish'), ('Schedule', 'Schedule'), ('Close', 'Close')], default='Pending', help_text='Select Category', max_length=10)),
            ],
            options={
                'ordering': ['name'],
            },
        ),
        migrations.CreateModel(
            name='Department',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(help_text='Enter name of section(eg. Maintenance)', max_length=50, null=True)),
                ('initial', models.CharField(help_text='Enter initial of section(eg. Mntc)', max_length=5, null=True)),
                ('description', models.CharField(help_text='Enter description of department', max_length=200, null=True)),
            ],
            options={
                'ordering': ['name'],
            },
        ),
        migrations.CreateModel(
            name='Mode',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(blank=True, choices=[('Forward', 'Forward'), ('Reverse', 'Reverse'), ('Stay', 'Stay')], default='Forward', help_text='Select Mode', max_length=10)),
            ],
            options={
                'ordering': ['name'],
            },
        ),
        migrations.AddField(
            model_name='cmmsuser',
            name='forward_path',
            field=models.IntegerField(null=True),
        ),
        migrations.AddField(
            model_name='cmmsuser',
            name='reverse_path',
            field=models.IntegerField(null=True),
        ),
        migrations.CreateModel(
            name='Section',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(help_text='Enter name of section(eg. Electrical & Instrumentation)', max_length=50, null=True)),
                ('description', models.CharField(help_text='Enter description of section', max_length=200, null=True)),
                ('department', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='accounts.department')),
            ],
            options={
                'ordering': ['department', 'name'],
            },
        ),
        migrations.CreateModel(
            name='Action',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(help_text='Enter name of Action(eg. Open, Close, Reject...)', max_length=20, null=True)),
                ('description', models.CharField(help_text='Enter description of Action', max_length=100, null=True)),
                ('category', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='accounts.category')),
                ('mode', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='accounts.mode')),
            ],
            options={
                'ordering': ['name'],
            },
        ),
        migrations.AddField(
            model_name='cmmsuser',
            name='actions',
            field=models.ManyToManyField(help_text='Select actions', to='accounts.Action'),
        ),
        migrations.AddField(
            model_name='cmmsuser',
            name='section',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='accounts.section'),
        ),
    ]
