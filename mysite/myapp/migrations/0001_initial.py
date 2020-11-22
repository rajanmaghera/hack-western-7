# Generated by Django 3.1.3 on 2020-11-21 21:28

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Person',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('person_name', models.CharField(default='', max_length=20)),
                ('person_text', models.CharField(default='', max_length=200)),
            ],
        ),
        migrations.CreateModel(
            name='Schedule',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('schedule_item', models.CharField(default='no text', max_length=200)),
                ('schedule_time', models.TimeField()),
                ('person', models.ForeignKey(default='Nobody', on_delete=django.db.models.deletion.CASCADE, to='myapp.person')),
            ],
        ),
        migrations.CreateModel(
            name='Post',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('post_img', models.ImageField(default='No picture', upload_to=None)),
                ('post_text', models.CharField(default='no text', max_length=200)),
                ('posted_time', models.DateTimeField(verbose_name='previous time')),
                ('person', models.ForeignKey(default='Nobody', on_delete=django.db.models.deletion.CASCADE, to='myapp.person')),
            ],
        ),
        migrations.CreateModel(
            name='Comment',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('comment_text', models.CharField(default='', max_length=200)),
                ('post', models.ForeignKey(default='Nothing', on_delete=django.db.models.deletion.CASCADE, to='myapp.post')),
            ],
        ),
    ]