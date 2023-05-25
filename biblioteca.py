class Livro:
    def __init__(self, titulo, autor, editora, categoria, num_copias):
        self.titulo = titulo
        self.autor = autor
        self.editora = editora
        self.categoria = categoria
        self.num_copias = num_copias

    def emprestar(self):
        if self.num_copias > 0:
            self.num_copias -= 1
            return True
        else:
            return False

    def devolver(self):
        self.num_copias += 1


class Biblioteca:
    def __init__(self):
        self.livros = []

    def adicionar_livro(self, livro):
        self.livros.append(livro)

    def mostrar_livros_disponiveis(self):
        for livro in self.livros:
            if livro.num_copias > 0:
                print(f"Título: {livro.titulo}")
                print(f"Autor: {livro.autor}")
                print(f"Editora: {livro.editora}")
                print(f"Categoria: {livro.categoria}")
                print(f"Número de cópias disponíveis: {livro.num_copias}")
                print()

    def buscar_livro(self, termo):
        for livro in self.livros:
            if (
                termo.lower() in livro.titulo.lower()
                or termo.lower() in livro.autor.lower()
                or termo.lower() in livro.categoria.lower()
            ):
                print(f"Título: {livro.titulo}")
                print(f"Autor: {livro.autor}")
                print(f"Editora: {livro.editora}")
                print(f"Categoria: {livro.categoria}")
                print(f"Número de cópias disponíveis: {livro.num_copias}")
                print()

    def emprestar_livro(self, livro):
        if livro.emprestar():
            print(f"O livro '{livro.titulo}' foi emprestado com sucesso.")
        else:
            print(f"Não há cópias disponíveis do livro '{livro.titulo}'.")

    def devolver_livro(self, livro):
        livro.devolver()
        print(f"O livro '{livro.titulo}' foi devolvido com sucesso.")


class Usuario:
    def __init__(self, nome):
        self.nome = nome
        self.historico_emprestimos = []

    def emprestar_livro(self, biblioteca, livro):
        biblioteca.emprestar_livro(livro)
        self.historico_emprestimos.append(livro)

    def devolver_livro(self, biblioteca, livro):
        biblioteca.devolver_livro(livro)
        self.historico_emprestimos.remove(livro)

    def ver_historico_emprestimos(self):
        if self.historico_emprestimos:
            print("Histórico de Empréstimos:")
            for livro in self.historico_emprestimos:
                print(f"Título: {livro.titulo}")
                print(f"Autor: {livro.autor}")
                print(f"Editora: {livro.editora}")
                print(f"Categoria: {livro.categoria}")
                print()
        else:
            print("Você ainda não realizou nenhum empréstimo.")


# Exemplo de uso:

# Criando a biblioteca
biblioteca = Biblioteca()

# Criando livros
livro1 = Livro("Python Crash Course", "Eric Matthes", "No Starch Press", "Programação", 3)
livro2 = Livro("Clean Code", "Robert C. Martin", "Prentice Hall", "Programação", 2)
livro3 = Livro("A Brief History of Time", "Stephen Hawking", "Bantam Books", "Ciência", 1)

# Adicionando livros à biblioteca
biblioteca.adicionar_livro(livro1)
biblioteca.adicionar_livro(livro2)
biblioteca.adicionar_livro(livro3)

# Criando usuário
usuario = Usuario("João")

# Visualizando livros disponíveis
biblioteca.mostrar_livros_disponiveis()

# Buscando livros por autor
print("Buscando livros por autor:")
biblioteca.buscar_livro("Eric")

# Empréstimo de livro
usuario.emprestar_livro(biblioteca, livro1)
usuario.emprestar_livro(biblioteca, livro2)
usuario.emprestar_livro(biblioteca, livro3)

# Verificando histórico de empréstimos do usuário
usuario.ver_historico_emprestimos()

# Devolução de livro
usuario.devolver_livro(biblioteca, livro1)

# Verificando histórico de empréstimos atualizado
usuario.ver_historico_emprestimos()

# Visualizando livros disponíveis após devolução
print("Livros disponíveis após devolução:")
biblioteca.mostrar_livros_disponiveis()
