# Use include () para adicionar caminhos do aplicativo de catálogo

from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('livros/', views.LivroListView.as_view(), name='livros'),
    path('livro/<int:pk>', views.LivroDetailView.as_view(), name='detalhe-do-livro')

]