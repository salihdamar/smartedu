# Generated by Django 5.0.7 on 2024-08-03 17:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('courses', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='course',
            name='image',
            field=models.ImageField(default='courses/defult_course_image.jpg', upload_to='courses/%Y/%m/%d/'),
        ),
    ]