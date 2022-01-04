from django.shortcuts import render

# Create your views here.
from .models import Livro, InstanciaDoLivro, Autor, Genero
from django.views import generic


def index(request):
    """Função de visualização da página inicial do site."""

    # Gerar contagens de alguns dos objetos principais
    num_livros = Livro.objects.all().count()
    li_todos = InstanciaDoLivro.objects.all().count()

    # Livros disponíveis (status = 'd')
    li_disponivel = InstanciaDoLivro.objects.filter(status__exact='d').count()

    # O 'all()' é implícito por padrão.
    num_autores = Autor.objects.count()

    num_genero = Genero.objects.count()

    context = {
        'num_livros': num_livros,
        'li_todos': li_todos,
        'li_disponivel': li_disponivel,
        'num_autores': num_autores,
        'num_genero': num_genero,
    }

    # Renderiza o template HTML index.html com os dados da variável de context
    return render(request, 'index.html', context=context)

class LivroListView(generic.ListView):
    model = Livro

    def get_context_data(self, **kwargs):
        # Chame a implementação de base primeiro para obter o contexto
        context = super(LivroListView, self).get_context_data(**kwargs)
        # Crie quaisquer dados e adicione-os ao contexto
        context['some_data'] = 'Estes são apenas alguns dados'
        return context

class LivroDetailView(generic.DetailView):
    model = Livro
