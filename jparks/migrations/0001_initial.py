# Generated by Django 2.1.5 on 2019-04-24 20:04

from decimal import Decimal
from django.conf import settings
import django.contrib.auth.models
import django.contrib.auth.validators
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone
import djmoney.models.fields


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('auth', '0009_alter_user_last_name_max_length'),
    ]

    operations = [
        migrations.CreateModel(
            name='CustomUser',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('password', models.CharField(max_length=128, verbose_name='password')),
                ('last_login', models.DateTimeField(blank=True, null=True, verbose_name='last login')),
                ('is_superuser', models.BooleanField(default=False, help_text='Designates that this user has all permissions without explicitly assigning them.', verbose_name='superuser status')),
                ('username', models.CharField(error_messages={'unique': 'A user with that username already exists.'}, help_text='Required. 150 characters or fewer. Letters, digits and @/./+/-/_ only.', max_length=150, unique=True, validators=[django.contrib.auth.validators.UnicodeUsernameValidator()], verbose_name='username')),
                ('first_name', models.CharField(blank=True, max_length=30, verbose_name='first name')),
                ('last_name', models.CharField(blank=True, max_length=150, verbose_name='last name')),
                ('email', models.EmailField(blank=True, max_length=254, verbose_name='email address')),
                ('is_staff', models.BooleanField(default=False, help_text='Designates whether the user can log into this admin site.', verbose_name='staff status')),
                ('is_active', models.BooleanField(default=True, help_text='Designates whether this user should be treated as active. Unselect this instead of deleting accounts.', verbose_name='active')),
                ('date_joined', models.DateTimeField(default=django.utils.timezone.now, verbose_name='date joined')),
                ('license_plate', models.CharField(max_length=255, null=True)),
                ('phone_number', models.CharField(max_length=255, null=True)),
                ('balance_currency', djmoney.models.fields.CurrencyField(choices=[('CAD', 'CAD $')], default='CAD', editable=False, max_length=3)),
                ('balance', djmoney.models.fields.MoneyField(decimal_places=2, default=Decimal('0.0'), default_currency='CAD', max_digits=14)),
                ('groups', models.ManyToManyField(blank=True, help_text='The groups this user belongs to. A user will get all permissions granted to each of their groups.', related_name='user_set', related_query_name='user', to='auth.Group', verbose_name='groups')),
                ('user_permissions', models.ManyToManyField(blank=True, help_text='Specific permissions for this user.', related_name='user_set', related_query_name='user', to='auth.Permission', verbose_name='user permissions')),
            ],
            options={
                'verbose_name': 'user',
                'verbose_name_plural': 'users',
                'abstract': False,
            },
            managers=[
                ('objects', django.contrib.auth.models.UserManager()),
            ],
        ),
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('zone_price_currency', djmoney.models.fields.CurrencyField(choices=[('CAD', 'CAD $')], default='XYZ', editable=False, max_length=3)),
                ('zone_price', djmoney.models.fields.MoneyField(choices=[('5', 'zone_1'), ('3', 'zone_2'), ('1', 'zone_3')], decimal_places=2, default=Decimal('0.0'), max_digits=14)),
            ],
        ),
        migrations.CreateModel(
            name='Owner',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
            ],
        ),
        migrations.CreateModel(
            name='Parking',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('street_type', models.CharField(choices=[('ST', 'Street'), ('AVE', 'Avenue'), ('BLVD', 'Boulevard'), ('RD', 'Road')], default='ST', max_length=4)),
                ('street_name', models.CharField(max_length=255)),
                ('street_number', models.IntegerField()),
                ('zip_code', models.CharField(max_length=6)),
                ('province', models.CharField(choices=[('BC', 'British Columbia'), ('MB', 'Manitoba'), ('NB', 'New Brunswick'), ('NL', 'Newfoundland and Labrador'), ('NT', 'Northwest Territories'), ('NS', 'Nova Scotia'), ('NU', 'Nunavut'), ('ON', 'Ontario'), ('PE', 'Prince Edward Island'), ('QC', 'Québec'), ('SK', 'Saskatchewan'), ('YT', 'Yukon')], default='ON', max_length=255)),
                ('city', models.CharField(max_length=255)),
                ('image', models.URLField(max_length=255, null=True)),
                ('phone', models.IntegerField()),
                ('description', models.TextField(null=True)),
                ('opening_time', models.TimeField()),
                ('closing_time', models.TimeField()),
                ('hourly_rate', models.IntegerField()),
            ],
            options={
                'permissions': (('can_edit_parking', 'User Can edit Parking'),),
            },
        ),
        migrations.CreateModel(
            name='Reservation',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('starting_date', models.DateField()),
                ('ending_date', models.DateField()),
                ('starting_time', models.TimeField()),
                ('ending_time', models.TimeField()),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('notes', models.TextField(blank=True)),
                ('User', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='reservations_made', to=settings.AUTH_USER_MODEL)),
                ('parking', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='reservations', to='jpark.Parking')),
            ],
        ),
        migrations.AddField(
            model_name='parking',
            name='drivers',
            field=models.ManyToManyField(related_name='reserved_parking_lots', through='jpark.Reservation', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='parking',
            name='owner',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='owned_parking_lots', to=settings.AUTH_USER_MODEL),
        ),
    ]
