# Generated by Django 2.0 on 2024-10-19 07:11

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('AptitudeApp', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Complaint',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('complaint_description', models.CharField(max_length=50)),
                ('complaint_date', models.CharField(max_length=50)),
                ('complaint_reply', models.CharField(max_length=50)),
                ('complaint_status', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='Education_Content',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=50)),
                ('description', models.CharField(max_length=50)),
                ('file_type', models.CharField(max_length=50)),
                ('file_path', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='Feedback',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('feedback_description', models.CharField(max_length=50)),
                ('feedback_date', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='Questions',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('question', models.CharField(max_length=50)),
                ('option1', models.CharField(max_length=50)),
                ('option2', models.CharField(max_length=50)),
                ('option3', models.CharField(max_length=50)),
                ('option4', models.CharField(max_length=50)),
                ('question_type', models.CharField(max_length=50)),
                ('question_mark', models.CharField(max_length=50)),
                ('question_level', models.CharField(max_length=50)),
                ('answer_description', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='Result',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('answer', models.CharField(max_length=50)),
                ('mark', models.CharField(max_length=50)),
                ('result_date', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='Test',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('test_name', models.CharField(max_length=50)),
                ('test_date', models.CharField(max_length=50)),
                ('test_description', models.CharField(max_length=50)),
                ('test_status', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='Test_Question',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('QUESTIONS', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='AptitudeApp.Questions')),
                ('TEST', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='AptitudeApp.Test')),
            ],
        ),
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('email', models.CharField(max_length=50)),
                ('phone', models.CharField(max_length=50)),
                ('gender', models.CharField(max_length=50)),
                ('dob', models.CharField(max_length=50)),
                ('place', models.CharField(max_length=50)),
                ('photo', models.CharField(max_length=50)),
                ('LOGIN', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='AptitudeApp.Login')),
            ],
        ),
        migrations.AddField(
            model_name='result',
            name='TESTQUESTION',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='AptitudeApp.Test_Question'),
        ),
        migrations.AddField(
            model_name='result',
            name='USER',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='AptitudeApp.User'),
        ),
        migrations.AddField(
            model_name='feedback',
            name='USER',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='AptitudeApp.User'),
        ),
        migrations.AddField(
            model_name='complaint',
            name='USER',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='AptitudeApp.User'),
        ),
    ]
