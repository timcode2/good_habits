# Generated by Django 4.2.7 on 2023-11-18 12:33

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Habit',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('place', models.CharField(max_length=255, verbose_name='Место')),
                ('habit_time', models.TimeField(verbose_name='Время выполнения')),
                ('action', models.CharField(max_length=255, verbose_name='Действие')),
                ('is_pleasant', models.BooleanField(verbose_name='Приятная привычка')),
                ('periodicity', models.IntegerField(verbose_name='Периодичность')),
                ('award', models.CharField(blank=True, max_length=255, null=True, verbose_name='Вознаграждение')),
                ('execution_time', models.DurationField(verbose_name='Время выполнения')),
                ('is_public', models.BooleanField(default=False, verbose_name='Публичность')),
                ('last_execution_time', models.DateTimeField(blank=True, null=True, verbose_name='Время последнего выполнения привычки')),
                ('related_habit', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='spa.habit', verbose_name='Связанная привычка')),
            ],
        ),
    ]
