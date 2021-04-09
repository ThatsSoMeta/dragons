# Generated by Django 3.1.7 on 2021-04-09 19:52

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
            name='CharacterDescriptions',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('personality', models.CharField(max_length=255)),
                ('apperance', models.CharField(max_length=255)),
                ('backstory', models.CharField(max_length=255)),
            ],
        ),
        migrations.CreateModel(
            name='SpellSheet',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('spell_name', models.CharField(max_length=60)),
                ('spell_type', models.CharField(max_length=40)),
                ('casting_time', models.CharField(max_length=25)),
                ('spell_range', models.IntegerField()),
                ('spell_components', models.CharField(max_length=200)),
                ('spell_duration', models.IntegerField()),
                ('spell_description', models.CharField(max_length=200)),
            ],
        ),
        migrations.CreateModel(
            name='CharacterSheet',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('level', models.IntegerField(default=1)),
                ('class_name', models.CharField(choices=[('barbarian', 'barbarian'), ('bard', 'bard'), ('cleric', 'cleric'), ('druid', 'druid'), ('fighter', 'fighter'), ('monk', 'monk'), ('paladin', 'paladin'), ('ranger', 'ranger'), ('rogue', 'rogue'), ('sorcerer', 'sorcerer'), ('warlock', 'warlock'), ('wizard', 'wizard'), ('artificer', 'artificer')], default=None, max_length=25)),
                ('race', models.CharField(choices=[('dragonborn', 'dragonborn'), ('dwarf', 'dwarf'), ('elf', 'elf'), ('gnome', 'gnome'), ('half-elf', 'half-elf'), ('half-orc', 'half-orc'), ('halfling', 'halfling'), ('human', 'human'), ('tiefling', 'tiefling')], default=None, max_length=20)),
                ('alignment', models.CharField(choices=[('lawful-good', 'lawful-good'), ('neutral-good', 'neutral-good'), ('chaotic-good', 'chaotic-good'), ('lawful-neutral', 'lawful-neutral'), ('neutral', 'neutral'), ('chaotic-neutral', 'chaotic-neutral'), ('lawful-evil', 'lawful-evil'), ('neutral-evil', 'neutral-evil'), ('chaotic-evil', 'chaotic-evil')], default=None, max_length=25)),
                ('background', models.CharField(blank=True, max_length=25, null=True)),
                ('proficiency_bonus', models.IntegerField(default=0)),
                ('armorclass', models.IntegerField(default=0)),
                ('speed', models.IntegerField(default=0)),
                ('hp', models.IntegerField(default=0)),
                ('temp_hp', models.IntegerField(default=0)),
                ('feats_traits', models.CharField(blank=True, max_length=255, null=True)),
                ('equipment', models.CharField(blank=True, max_length=255, null=True)),
                ('languages', models.CharField(blank=True, max_length=255, null=True)),
                ('player', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
