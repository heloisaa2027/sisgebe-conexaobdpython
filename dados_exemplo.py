# dados_exemplo.py
from crud.crud_livro import criar_livro
from crud.crud_aluno import criar_aluno
from crud.crud_professor import criar_professor
from crud.crud_bibliotecario import criar_bibliotecario
from crud.crud_diretor import criar_diretor
from crud.crud_supervisor import criar_supervisor
from crud.crud_reserva import criar_reserva
from crud.crud_emprestimo import criar_emprestimo
from crud.crud_sugestao import criar_sugestao
from crud.crud_historicoleitura import criar_historico
from crud.crud_relatorio import criar_relatorio
from crud.crud_livro import criar_livro as ci_livro
from crud.crud_livro import listar_livros

def popular():
    # categorias (assume que Categoria CRUD existe; se ainda não, insira direto em SQL)
    # livros
    ci_livro("Dom Casmurro", "Machado de Assis", isbn="9783575412621", sinopse="Romance clássico", capa=None, quantidade=3, categoria_id=None)
    ci_livro("A Hora da Estrela", "Clarice Lispector", isbn="9788535911500", sinopse="Romance", capa=None, quantidade=2, categoria_id=None)

# alunos
criar_aluno("João Silva", "joao@escola.local", "senha123", "9A")
criar_aluno("Maria Oliveira", "maria@escola.local", "senha123", "8B")

#  professores
criar_professor("Carlos Souza", "carlos@escola.local", "senha123", disciplina="História")
criar_professor("Patricia Lima", "patricia@escola.local", "senha123", disciplina="portguês")

# bibliotecário / diretor /supervisor