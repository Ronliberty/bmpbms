# Generated by Django 4.2.16 on 2024-11-23 15:13

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='PartnershipArea',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255, unique=True)),
                ('description', models.TextField(blank=True, null=True)),
                ('created_by', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='created_Partnership', to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='PartnershipRequest',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('status', models.CharField(choices=[('pending', 'Pending'), ('reviewed', 'Reviewed'), ('accepted', 'Accepted'), ('rejected', 'Rejected')], default='pending', max_length=10)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('created_by', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='created_requests', to=settings.AUTH_USER_MODEL)),
                ('partnership_area', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='requests', to='partner.partnershiparea')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='partnership_requests', to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='PartnershipQuestion',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('question_text', models.TextField()),
                ('partnership_area', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='questions', to='partner.partnershiparea')),
            ],
        ),
        migrations.CreateModel(
            name='PartnershipEngagement',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('start_date', models.DateField(auto_now_add=True)),
                ('notes', models.TextField(blank=True, null=True)),
                ('manager', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='engagements', to=settings.AUTH_USER_MODEL)),
                ('partnership_reqeust', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='engagements', to='partner.partnershiprequest')),
            ],
        ),
        migrations.CreateModel(
            name='PartnershipAnswer',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('answer_text', models.TextField()),
                ('partnership_reqeust', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='answers', to='partner.partnershiprequest')),
                ('question', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='answers', to='partner.partnershipquestion')),
            ],
        ),
    ]
