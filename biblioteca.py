class Livro:
    def __init__(self, titulo, autor, editora, categoria, num_copias):
        self.titulo = titulo
        self.autor = autor
        self.editora = editora
        self.categoria = categoria
        self.num_copias = num_copias

    def emprestar(self):
        pass

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
        pass

    def devolver_livro(self, livro):
       pass


class Usuario:
    def __init__(self, nome):
        self.nome = nome
        self.historico_emprestimos = []

    def emprestar_livro(self, biblioteca, livro):
        pass

    def devolver_livro(self, biblioteca, livro):
        pass

    def ver_historico_emprestimos(self):
        pass
    
        #else:
            #print("Você ainda não realizou nenhum empréstimo.")
