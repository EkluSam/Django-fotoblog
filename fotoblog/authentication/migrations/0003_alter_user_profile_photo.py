# Generated by Django 5.0.2 on 2024-03-04 10:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('authentication', '0002_alter_user_profile_photo_alter_user_role'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='profile_photo',
            field=models.ImageField(default='unknown.jpg', upload_to='profile_pics', verbose_name='photo de profil'),
        ),
    ]