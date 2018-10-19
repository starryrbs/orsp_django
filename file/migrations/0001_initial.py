# Generated by Django 2.1.1 on 2018-10-17 19:49

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('user', '0008_auto_20181013_1124'),
    ]

    operations = [
        migrations.CreateModel(
            name='Resource',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('download_count', models.IntegerField(default=0)),
                ('need_integral', models.IntegerField(default=0)),
                ('upload_time', models.DateTimeField(auto_now_add=True)),
                ('like_num', models.IntegerField(default=0)),
                ('share_num', models.IntegerField(default=0)),
                ('title', models.CharField(max_length=80, null=True)),
                ('upload_user', models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='user.User')),
            ],
        ),
    ]