# Generated by Django 3.2.10 on 2022-01-02 23:53

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('catalogo', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Linguagem',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(help_text='Digite o idioma natural do livro (por exemplo, inglês, francês, japonês etc.)', max_length=200)),
            ],
        ),
        migrations.AddField(
            model_name='livro',
            name='linguagem',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='catalogo.linguagem'),
        ),
    ]
