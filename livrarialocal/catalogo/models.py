import uuid

from django.db import models

# Create your models here.
from django.urls import reverse


class Genero(models.Model):
    """Este Model representa o genero de Livros """
    nome = models.CharField(max_length=200, help_text='Insira o gênero de um livro (por exemplo, ficção científica)')

    class Meta:
        verbose_name = "Genero"
        verbose_name_plural = "Generos"

    def __str__(self):
        """String para representar o objeto Model"""
        return self.nome

class Linguagem(models.Model):
    """Modelo que representa um idioma (por exemplo, inglês, francês, japonês etc.)"""
    nome = models.CharField(max_length=200,
                            help_text='Digite o idioma natural do livro (por exemplo, inglês, francês, japonês etc.)')

    class Meta:
        verbose_name = "Linguagem"
        verbose_name_plural = "Linguagens"

    def __str__(self):
        """String para representar o objeto Model (no site Admin etc.)"""
        return self.nome



class Livro(models.Model):
    """Modelo que representa um livro (mas não uma cópia específica de um livro)."""
    titulo = models.CharField(max_length=200)
    # Chave estrangeira usada porque o livro pode ter apenas um autor, mas os autores podem ter vários livros
    autor = models.ForeignKey('Autor', on_delete=models.SET_NULL, null=True)

    resumo = models.TextField(max_length=1000, help_text='Insira uma breve descrição do livro')
    isbn = models.CharField('ISBN', max_length=13, help_text='13 Personagem <a href="https://www.cblservicos.org.br/isbn/">número ISBN</a>')

    genero = models.ManyToManyField(Genero, help_text='Selecione um gênero para este livro')
    # ManyToManyField usado porque o gênero pode conter muitos livros. Os livros podem abranger muitos gêneros.
    # A classe de gênero já foi definida para que possamos especificar o objeto acima.
    linguagem = models.ForeignKey('Linguagem', on_delete=models.SET_NULL, null=True)

    # Foto do Livro
    foto = models.ImageField(upload_to='images/%Y/%m/%d', blank=True, null=True, verbose_name='Foto do Livro')

    class Meta:
        verbose_name = "Livro"
        verbose_name_plural = "Livros"

    def display_genero(self):
        """Crie uma string para o gênero. Isso é necessário para exibir o gênero no Admin."""
        return ','.join(genero.nome for genero in self.genero.all()[:3])
    display_genero.short_description = 'Genero'

    def __str__(self):
        """String para representar o objeto Model."""
        return self.titulo

    def get_absolute_url(self):
        """Retorna o url para acessar um registro de detalhes deste livro."""
        return reverse('detalhe-do-livro', args=[str(self.id)])

class InstanciaDoLivro(models.Model):
    """Modelo que representa uma cópia específica de um livro (ou seja, pode ser emprestado na biblioteca)."""
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, help_text='ID exclusivo para este livro específico em toda a biblioteca')
    livro = models.ForeignKey('Livro', on_delete=models.SET_NULL, null=True)
    publicado = models.CharField(max_length=200)
    data_retorno = models.DateField(null=True, blank=True)

    ESTATUS_EMPRESTIMO = (
        ('m', 'Manutenção'),
        ('p', 'Por empréstimo'),
        ('d', 'Disponível'),
        ('r', 'Reservado'),
    )

    status = models.CharField(
        max_length=1,
        choices=ESTATUS_EMPRESTIMO,
        blank=True,
        default='m',
        help_text='Disponibilidade dos livros',
    )

    class Meta:
        verbose_name = "Instancia Do Livro"
        verbose_name_plural = "Instancia Dos Livros"
        ordering = ['data_retorno']

    def __str__(self):
        """String para representar o objeto Model."""
        return f'{self.id} ({self.livro.titulo})'

class Autor(models.Model):
    """Modelo que representa um autor."""
    primeiro_nome = models.CharField(max_length=100)
    sobre_nome = models.CharField(max_length=100)
    data_de_nascimento = models.DateField(null=True, blank=True)
    data_da_morte = models.DateField('Faleceu', null=True, blank=True)

    class Meta:
        verbose_name = "Autor"
        verbose_name_plural = "Autores"
        ordering = ['sobre_nome', 'primeiro_nome']

    def get_absolute_url(self):
        """Retorna o url para acessar uma instância particular do autor."""
        return reverse('autor-detail', args=[str(self.id)])

    def __str__(self):
        """String para representar o objeto Model."""
        return f' {self.primeiro_nome}, {self.sobre_nome}'