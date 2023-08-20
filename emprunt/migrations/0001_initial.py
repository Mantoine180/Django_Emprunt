# Generated by Django 4.2.4 on 2023-08-16 16:13

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Budget',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('type_budget', models.CharField(choices=[('AC', 'Année courante'), ('PR', 'Projets'), ('FE', 'Financements exceptionnels')], max_length=2)),
            ],
        ),
        migrations.CreateModel(
            name='Enseignant',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nom', models.CharField(max_length=200)),
                ('prenom', models.CharField(max_length=200)),
            ],
        ),
        migrations.CreateModel(
            name='Salle',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('numero', models.CharField(max_length=10)),
            ],
        ),
        migrations.CreateModel(
            name='Matériel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nom', models.CharField(max_length=255)),
                ('acheteur', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='achats', to='emprunt.enseignant')),
                ('budget', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='emprunt.budget')),
                ('possesseur', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='emprunts', to='emprunt.enseignant')),
                ('proprietaire', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='matériels', to='emprunt.enseignant')),
                ('salle', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='matériels', to='emprunt.salle')),
            ],
        ),
        migrations.CreateModel(
            name='Emprunt',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date_emprunt', models.DateTimeField()),
                ('date_retour', models.DateTimeField(blank=True, null=True)),
                ('lieu', models.CharField(max_length=255)),
                ('occasion', models.CharField(max_length=255)),
                ('objectif_utilisation', models.TextField()),
                ('enseignant_emprunteur', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='emprunt.enseignant')),
                ('matériel', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='emprunt.matériel')),
            ],
        ),
        migrations.CreateModel(
            name='Accessoire',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nom', models.CharField(max_length=255)),
                ('etat', models.CharField(choices=[('NE', 'Neuf'), ('US', 'Usé'), ('EN', 'Endommagé')], max_length=2)),
                ('matériel', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='accessoires', to='emprunt.matériel')),
            ],
        ),
    ]
