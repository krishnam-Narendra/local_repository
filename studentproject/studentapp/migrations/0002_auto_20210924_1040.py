# Generated by Django 3.2 on 2021-09-24 05:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('studentapp', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='ProxyStudentRegister',
            fields=[
            ],
            options={
                'proxy': True,
                'indexes': [],
                'constraints': [],
            },
            bases=('studentapp.studentregister',),
        ),
        migrations.AlterField(
            model_name='marksdetails',
            name='NS',
            field=models.IntegerField(verbose_name='Natural Science'),
        ),
        migrations.AlterField(
            model_name='marksdetails',
            name='PS',
            field=models.IntegerField(verbose_name='Pysical Science'),
        ),
        migrations.AlterField(
            model_name='marksdetails',
            name='course',
            field=models.CharField(max_length=60, verbose_name='Enter Course Name'),
        ),
        migrations.AlterField(
            model_name='marksdetails',
            name='father_name',
            field=models.CharField(max_length=60, verbose_name='Enter Your Father Name'),
        ),
        migrations.AlterField(
            model_name='marksdetails',
            name='fname',
            field=models.CharField(max_length=60, verbose_name='Enter First Name'),
        ),
        migrations.AlterField(
            model_name='marksdetails',
            name='lname',
            field=models.CharField(max_length=60, verbose_name='Enter Last Name'),
        ),
        migrations.AlterField(
            model_name='marksdetails',
            name='school_name',
            field=models.CharField(max_length=60, verbose_name='Enter School Name'),
        ),
        migrations.AlterField(
            model_name='studentregister',
            name='course',
            field=models.CharField(max_length=60, verbose_name='Enter Course Name'),
        ),
        migrations.AlterField(
            model_name='studentregister',
            name='email',
            field=models.EmailField(max_length=254, verbose_name='Enter Email'),
        ),
        migrations.AlterField(
            model_name='studentregister',
            name='father_name',
            field=models.CharField(max_length=60, verbose_name='Enter Your Father Name'),
        ),
        migrations.AlterField(
            model_name='studentregister',
            name='fname',
            field=models.CharField(max_length=60, verbose_name='Enter First Name'),
        ),
        migrations.AlterField(
            model_name='studentregister',
            name='lname',
            field=models.CharField(max_length=60, verbose_name='Enter Last Name'),
        ),
        migrations.AlterField(
            model_name='studentregister',
            name='roolno',
            field=models.IntegerField(verbose_name='Enter Rool Number'),
        ),
        migrations.AlterField(
            model_name='studentregister',
            name='school_name',
            field=models.CharField(max_length=60, verbose_name='Enter School Name'),
        ),
    ]
