import time

class Livro:
    def __init__(self, titulo, autor, code, ano_publicacao):
        self.titulo = titulo
        self.autor = autor
        self.code = code
        self.ano_publicacao = ano_publicacao
        self.disponivel = True
        self.categoria = ""

class Biblioteca:
    def __init__(self):
        self.livros = []

    def adicionar_livro(self, livro):
        if livro.code in [livro.code for livro in self.livros]:
            print('O Código do Livro já existe na biblioteca')
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

    def buscar_livro_por_code(self, code):
        for livro in self.livros:
            if livro.code == code:
                return livro
        return None

    def buscar_livros_por_categoria(self, categoria):
        livros_encontrados = []
        for livro in self.livros:
            if livro.categoria == categoria:
                livros_encontrados.append(livro)
        return livros_encontrados

    def listar_livros(self):
        for livro in self.livros:
            print(f"{livro.titulo} - {livro.autor} - Código do Livro: {livro.code} - Ano da Publicação: {livro.ano_publicacao} - Disponível: {livro.disponivel}")

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
                print(f"{livro.titulo} - {livro.autor} - Código do Livro: {livro.code} - Ano da Publicação: {livro.ano_publicacao}")

class LivroComum(Livro):
    pass

class LivroRaro(Livro):
    def __init__(self, titulo, autor, code, ano_publicacao, disponivel, edicao, estado):
        super().__init__(titulo, autor, code, ano_publicacao)
        self.edicao = edicao
        self.estado = estado

    def __str__(self):
        return f"{self.titulo}, {self.autor}, {self.code}, {self.ano_publicacao}, {self.disponivel}, {self.edicao}, {self.estado}"

class Usuario:
    def __init__(self, nome):
        self.nome = nome
        self.emprestimos = []

    def pegar_livro_emprestado(self, biblioteca, titulo):
        livro = biblioteca.buscar_livro_por_titulo(titulo)
        if livro is not None:
            try:
                biblioteca.registrar_emprestimo(livro)
                self.emprestimos.append(livro)
                print(f"{self.nome} pegou emprestado o livro '{livro.titulo}'.")
            except Exception as e:
                print(e)
        else:
            print("Livro não encontrado.")

    def devolver_livro(self, biblioteca, titulo):
        for livro in self.emprestimos:
            if livro.titulo == titulo:
                try:
                    biblioteca.registrar_devolucao(livro)
                    self.emprestimos.remove(livro)
                    print(f"{self.nome} devolveu o livro '{livro.titulo}'.")
                    return
                except Exception as e:
                    print(e)
        print("Livro não encontrado nos empréstimos do usuário.")

    def listar_emprestimos(self):
        if len(self.emprestimos) > 0:
            print(f"Empréstimos do usuário {self.nome}:")
            for livro in self.emprestimos:
                print(f"{livro.titulo} - {livro.autor} - Código do Livro: {livro.code} - Ano da Publicação: {livro.ano_publicacao}")
        else:
            print("O usuário não possui livros emprestados.")

def simbolizar_carregamento():
    """
    Exibe uma animação de carregamento.
    """
    for _ in range(4):
        for symbol in ['-', '\\', '|', '/']:
            print(f'Carregando {symbol}', end='\r')
            time.sleep(0.1)

biblioteca = Biblioteca()

# Criando objetos Livro
livro1 = LivroComum("Harry Potter e a Pedra Filosofal", "J.K. Rowling", "9788532530780", 1997)
livro2 = LivroComum("1984", "George Orwell", "9780451524935", 1949)
livro3 = LivroComum("O Senhor dos Anéis: A Sociedade do Anel", "J.R.R. Tolkien", "9788533615864", 1954)
livro4 = LivroRaro("A Origem das Espécies", "Charles Darwin", "9780140439120", 1859, True, "1ª edição", "Bom estado")

# Definindo categorias para os livros
livro1.categoria = "Fantasia"
livro2.categoria = "Ficção Científica"
livro3.categoria = "Fantasia"
livro4.categoria = "Ciências Naturais"

# Adicionando os livros à biblioteca
biblioteca.adicionar_livro(livro1)
biblioteca.adicionar_livro(livro2)
biblioteca.adicionar_livro(livro3)
biblioteca.adicionar_livro(livro4)

while True:
    print("=-" * 22)
    print("-- Sistema de Gerenciamento de Biblioteca --")
    print("=-" * 22)
    print(" ")
    print("              MENU:  ")
    print(" ")    
    print("1 - Adicionar um livro comum à biblioteca")
    print("2 - Adicionar um livro raro à biblioteca")
    print("3 - Remover um livro da biblioteca")
    print("4 - Buscar um livro na biblioteca")
    print("5 - Listar todos os livros da biblioteca")
    print("6 - Registrar um empréstimo de um livro")
    print("7 - Registrar a devolução de um livro")
    print("8 - Listar todos os livros emprestados")
    print("9 - Ver histórico de empréstimos do usuário")
    print("0 - Sair do programa")
    print(" ")
   
    opcao = input("Escolha uma opção: ")

    if opcao == "1":
        simbolizar_carregamento()
        titulo = input("Digite o título do livro: ")
        autor = input("Digite o nome do autor: ")
        code = input("Digite o Código do Livro do livro: ")
        ano_publicacao = input("Digite o ano de publicação do livro: ")
        livro = LivroComum(titulo, autor, code, ano_publicacao)
        biblioteca.adicionar_livro(livro)

    elif opcao == "2":
        simbolizar_carregamento()
        titulo = input("Digite o título do livro: ")
        autor = input("Digite o nome do autor: ")
        code = input("Digite o Código do Livro do livro: ")
        ano_publicacao = input("Digite o ano de publicação do livro: ")
        edicao = input("Digite a edição do livro raro: ")
        estado = input("Digite o estado do livro raro: ")
        livro = LivroRaro(titulo, autor, code, ano_publicacao, True, edicao, estado)
        biblioteca.adicionar_livro(livro)

    elif opcao == "3":
        simbolizar_carregamento()
        code = input("Digite o Código do Livro do livro que deseja remover: ")
        livro = biblioteca.buscar_livro_por_code(code)
        if Livro is not None:
            print(f"{Livro.titulo} - {Livro.autor} - Código do Livro: {Livro.code} - Ano da Publicação: {Livro.ano_publicacao}")
        else:
            print("Livro não encontrado na biblioteca.")

    elif opcao == "4":
        simbolizar_carregamento()
        criterio_busca = input("Digite o critério de busca (título, autor, Código do Livro ou categoria): ")
        termo_busca = input("Digite o termo de busca: ")
        if criterio_busca == "título":
            livro = biblioteca.buscar_livro_por_titulo(termo_busca)
        elif criterio_busca == "autor":
            livro = biblioteca.buscar_livro_por_autor(termo_busca)
        elif criterio_busca == "Código do Livro":
            livro = biblioteca.buscar_livro_por_code(termo_busca)
        elif criterio_busca == "categoria":
            livros_por_categoria = biblioteca.buscar_livros_por_categoria(termo_busca)
            if livros_por_categoria:
                print(f"Livros na categoria '{termo_busca}':")
                for livro in livros_por_categoria:
                    print(f"{livro.titulo} - {livro.autor} - ISBN: {livro.code} - Ano da Publicação: {livro.ano_publicacao}")
            else:
                print(f"Nenhum livro encontrado na categoria '{termo_busca}'.")
            continue

        if livro is not None:
            print(f"{livro.titulo} - {livro.autor} - ISBN: {livro.code} - Ano da Publicação: {livro.ano_publicacao}")
        else:
            print("Livro não encontrado na biblioteca.")

    elif opcao == "5":
        simbolizar_carregamento()
        biblioteca.listar_livros()

    elif opcao == "6":
        simbolizar_carregamento()
        titulo = input("Digite o título do livro que deseja pegar emprestado: ")
        usuario = Usuario("Usuário")
        usuario.pegar_livro_emprestado(biblioteca, titulo)

    elif opcao == "7":
        simbolizar_carregamento()
        titulo = input("Digite o título do livro que deseja devolver: ")
        usuario = Usuario("Usuário")
        usuario.devolver_livro(biblioteca, titulo)

    elif opcao == "8":
        simbolizar_carregamento()
        biblioteca.listar_livros_emprestados()

    elif opcao == "9":
        simbolizar_carregamento()
        usuario = Usuario("Usuário")
        usuario.listar_emprestimos()

    elif opcao == "0":
        print("Programa encerrado.")
        break

    else:
        print("Opção inválida. Digite um número correspondente à opção desejada.")
