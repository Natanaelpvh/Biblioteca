# Generated by Django 3.2 on 2022-01-18 13:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('catalogo', '0008_alter_livro_fotolivro'),
    ]

    operations = [
        migrations.AlterField(
            model_name='livro',
            name='fotoLivro',
            field=models.ImageField(blank=True, null=True, upload_to='images/%Y/%m/%d', verbose_name='Foto do Livro'),
        ),
    ]