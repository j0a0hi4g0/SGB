import time

class Livro:
    def __init__(self, titulo, autor, isbn, ano_publicacao):
        self.titulo = titulo
        self.autor = autor
        self.isbn = isbn
        self.ano_publicacao = ano_publicacao
        self.disponivel = True

class Biblioteca:
    def __init__(self):
        self.livros = []

    def adicionar_livro(self, livro):
        if livro.isbn in [livro.isbn for livro in self.livros]:
            print('O ISBN já existe na biblioteca')
        else:
            self.livros.append(livro)
            print('Livro adicionado à biblioteca.')

    def remover_livro(self, livro):
        self.livros.remove(livro)

    def buscar_livro_por_titulo(self, titulo):
        for livro in self.livros:
            if livro.titulo == titulo:
                return livro
        return None

    def buscar_livro_por_autor(self, autor):
        for livro in self.livros:
            if livro.autor == autor:
                return livro
        return None

    def buscar_livro_por_isbn(self, isbn):
        for livro in self.livros:
            if livro.isbn == isbn:
                return livro
        return None

    def listar_livros(self):
        for livro in self.livros:
            print(f"{livro.titulo} - {livro.autor} - ISBN: {livro.isbn} - Ano da Publicação: {livro.ano_publicacao}  - Disponível: {livro.disponivel}")

    def registrar_emprestimo(self, livro):
        if not livro.disponivel:
            raise Exception("Este livro já está emprestado.")
        livro.disponivel = False
        print("Empréstimo registrado.")

    def registrar_devolucao(self, livro):
        if livro.disponivel:
            raise Exception("Este livro já está disponível.")
        livro.disponivel = True
        print("Devolução registrada.")

    def listar_livros_emprestados(self):
        for livro in self.livros:
            if not livro.disponivel:
                print(f"{livro.titulo} - {livro.autor} - ISBN: {livro.isbn} - Ano da Publicação: {livro.ano_publicacao} ")

class LivroComum(Livro):
    pass

class LivroRaro(Livro):
    def __init__(self, titulo, autor, isbn, ano_publicacao, disponivel, edicao, estado):
        super().__init__(titulo, autor, isbn, ano_publicacao)
        self.edicao = edicao
        self.estado = estado

    def __str__(self):
        return f"{self.titulo}, {self.autor}, {self.isbn}, {self.ano_publicacao}, {self.disponivel}, {self.edicao}, {self.estado}"

def simbolizar_carregamento():
    """
    Exibe uma animação de carregamento.
    """
    for _ in range(4):
        for symbol in ['-', '\\', '|', '/']:
            print(f'Carregando {symbol}', end='\r')
            time.sleep(0.1)

biblioteca = Biblioteca()

while True:
    print("=-" *22)
    print("-- Sistema de Gerenciamento de Biblioteca --")
    print("=-" *22)
    print(" ")
    print("              MENU:  ")
    print(" ")    
    print("1 - Adicionar um livro comum à biblioteca")
    print("2 - Adicionar um livro raro à biblioteca")
    print("3 - Remover um livro da biblioteca")
    print("4 - Buscar um livro na biblioteca pelo título, autor ou ISBN")
    print("5 - Listar todos os livros da biblioteca")
    print("6 - Registrar um empréstimo de um livro")
    print("7 - Registrar a devolução de um livro")
    print("8 - Listar todos os livros emprestados")
    print("0 - Sair do programa")

    opcao = input()

    if opcao == "1":
        simbolizar_carregamento()
        titulo = input("Digite o título do livro: ")
        autor = input("Digite o autor do livro: ")
        isbn = input("Digite o ISBN do livro: ")
        ano_publicacao = input("Digite o Ano da publicação do livro: ")
        livro = LivroComum(titulo, autor, isbn, ano_publicacao)
        biblioteca.adicionar_livro(livro)

    elif opcao == "2":
        simbolizar_carregamento()
        titulo = input("Digite o título do livro: ")
        autor = input("Digite o autor do livro: ")
        isbn = input("Digite o ISBN do livro: ")
        ano_publicacao = input("Digite o Ano da publicação do livro: ")
        edicao = input("Digite a edição do livro: ")
        estado = input("Digite o estado do livro: ")
        livro = LivroRaro(titulo, autor, isbn, ano_publicacao, True, edicao, estado)
        biblioteca.adicionar_livro(livro)

    elif opcao == "3":
        simbolizar_carregamento()
        titulo = input("Digite o título do livro que deseja remover: ")
        livro = biblioteca.buscar_livro_por_titulo(titulo)
        if livro is not None:
            biblioteca.remover_livro(livro)
            print("Livro removido da biblioteca.")
        else:
            print("Livro não encontrado.")

    elif opcao == "4":
        simbolizar_carregamento()
        termo = input("Digite o termo que deseja buscar: ")
        livro = biblioteca.buscar_livro_por_titulo(termo)
        if livro is None:
            livro = biblioteca.buscar_livro_por_autor(termo)
        if livro is None:
            livro = biblioteca.buscar_livro_por_isbn(termo)
        if livro is not None:
            print(f"{livro.titulo} - {livro.autor} - ISBN: {livro.isbn} - Disponível: {livro.disponivel}")
        else:
            print("Livro não encontrado.")

    elif opcao == "5":
        simbolizar_carregamento()
        biblioteca.listar_livros()

    elif opcao == "6":
        simbolizar_carregamento()
        titulo = input("Digite o título do livro que deseja emprestar: ")
        livro = biblioteca.buscar_livro_por_titulo(titulo)
        if livro is not None:
            try:
                biblioteca.registrar_emprestimo(livro)
            except Exception as e:
                print(e)
        else:
            print("Livro não encontrado.")

    elif opcao == "7":
        simbolizar_carregamento()
        titulo = input("Digite o título do livro que deseja devolver: ")
        livro = biblioteca.buscar_livro_por_titulo(titulo)
        if livro is not None:
            try:
                biblioteca.registrar_devolucao(livro)
            except Exception as e:
                print(e)
        else:
            print("Livro não encontrado.")

    elif opcao == "8":
        simbolizar_carregamento()
        biblioteca.listar_livros_emprestados()

    elif opcao == "0":
        print("Obrigado por utilizar a biblioteca. Até mais!")
        break

    else:
        print("Opção inválida.")
