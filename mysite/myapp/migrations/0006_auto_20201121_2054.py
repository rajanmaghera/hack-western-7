# Generated by Django 3.1.3 on 2020-11-22 03:54

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0005_auto_20201121_1821'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='person',
            options={'ordering': ['person_name']},
        ),
        migrations.CreateModel(
            name='Friends',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('source', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='source', to='myapp.person')),
                ('target', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='target', to='myapp.person')),
            ],
        ),
        migrations.AddField(
            model_name='person',
            name='friends_list',
            field=models.ManyToManyField(through='myapp.Friends', to='myapp.Person'),
        ),
    ]