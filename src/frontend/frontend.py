import flet as ft
import backend.backend as be

class Tela:
    def __init__(self, page: ft.Page):
        self.page = page
        modoEscuro = self.page.platform_brightness.value == "dark"
        self.corFundo = ft.colors.WHITE if modoEscuro else ft.colors.BLACK
        self.corTexto = ft.colors.BLACK if modoEscuro else ft.colors.WHITE
        self.objetos()

    def objetos(self):
        self.estiloBotao = ft.ButtonStyle(bgcolor=self.corFundo,color=self.corTexto,shape=ft.RoundedRectangleBorder(radius=75),padding=20,text_style=ft.TextStyle(weight=ft.FontWeight.BOLD, size=26))
        self.campoUsuario = ft.TextField(label="Usuário", width=300, capitalization=ft.TextCapitalization.CHARACTERS)
        self.campoSenha = ft.TextField(label="Senha", width=300, password=True, can_reveal_password=True)
        self.botaoEntrar = ft.ElevatedButton("Entrar", width=300, on_click=lambda e: be.verificarValoresInput(self.page, self.campoUsuario, self.campoSenha, self.paginaInicial))
        self.botaoCadastrar = ft.ElevatedButton("Cadastrar", width=300, on_click=lambda e: self.cadastroCliente())
        self.botaoSair = ft.Container(content=ft.ElevatedButton(text="Sair", icon=ft.icons.ARROW_BACK, bgcolor=self.corFundo, color=self.corTexto, on_click=lambda e: self.telaLogin()), alignment=ft.alignment.top_left, padding=10)
        self.botaoSaqueIniciar = ft.ElevatedButton("SACAR", width=200, height=150, on_click=lambda e: self.telaSacar(), style=self.estiloBotao)
        self.botaoDepositoIniciar = ft.ElevatedButton("DEPOSITAR", width=200, height=150, on_click=lambda e: print("Ir para tela de depósito"), style=self.estiloBotao)
        self.botaoTransferenciaIniciar = ft.ElevatedButton("TRANSFERIR", width=200, height=150, on_click=lambda e: print("Ir para tela de transferência"), style=self.estiloBotao)
        self.campoRua = ft.TextField(label="Rua", width=300, capitalization=ft.TextCapitalization.CHARACTERS)
        self.campoBairro = ft.TextField(label="Bairro", width=300, capitalization=ft.TextCapitalization.CHARACTERS)
        self.campoCidade = ft.TextField(label="Cidade", width=300, capitalization=ft.TextCapitalization.CHARACTERS)
        self.campoUf = ft.TextField(label="UF", width=300, capitalization=ft.TextCapitalization.CHARACTERS)
        self.botoes = ft.Row(controls=[ft.ElevatedButton("Voltar", width=300, on_click=lambda e: self.telaLogin()),ft.ElevatedButton("Salvar", width=300, on_click=lambda e: self.aoSalvar())],alignment=ft.MainAxisAlignment.CENTER,spacing=30)
        self.campoNome = ft.TextField(label="Nome", width=300, capitalization=ft.TextCapitalization.WORDS, on_change=be.formatarNome)
        self.campoEmail = ft.TextField(label="Email", width=300, keyboard_type=ft.KeyboardType.EMAIL, on_change=be.validarEmail)
        self.campoCep = ft.TextField(label="CEP", width=300, keyboard_type=ft.KeyboardType.NUMBER, on_change=lambda e: be.validarCep(e, self.campoRua, self.campoBairro, self.campoCidade, self.campoUf))
        self.campoNumero = ft.TextField(label="Número", width=300, keyboard_type=ft.KeyboardType.NUMBER, on_change=be.somenteNumero)
        self.campoCpf = ft.TextField(label="CPF", width=300, keyboard_type=ft.KeyboardType.NUMBER, on_change=be.validarCpf)
        self.campoTelefone = ft.TextField(label="Telefone", width=300, keyboard_type=ft.KeyboardType.NUMBER, on_change=be.formatarTelefone)

    def configurarJanela(self, titulo: str, largura: int, altura: int, redimensionavel: bool = False):
        self.page.clean()
        self.page.title = titulo
        self.page.window.width = largura
        self.page.window.height = altura
        self.page.window.center()
        self.page.window.resizable = redimensionavel
        self.page.window.maximizable = False
        self.page.window.minimized = False
        self.page.vertical_alignment = ft.MainAxisAlignment.CENTER
        self.page.horizontal_alignment = ft.CrossAxisAlignment.CENTER

    def telaLogin(self):
        self.configurarJanela("Tela de Login", 350, 500)
        conteudo = ft.Container(content=ft.Column(controls=[self.campoUsuario, self.campoSenha, self.botaoEntrar, self.botaoCadastrar], alignment=ft.MainAxisAlignment.CENTER, horizontal_alignment=ft.CrossAxisAlignment.CENTER))
        self.page.add(conteudo)

    def paginaInicial(self):
        self.configurarJanela("Bem-vindo", 1000, 600)
        self.page.add(self.botaoSair, ft.Stack(controls=[ft.Container(content=ft.Row(controls=[self.botaoSaqueIniciar, self.botaoDepositoIniciar, self.botaoTransferenciaIniciar], alignment=ft.MainAxisAlignment.CENTER, spacing=30), alignment=ft.alignment.center, expand=True)], expand=True))

    def telaSacar(self):
        self.configurarJanela("Sacar", 1000, 600)
        valorSaque = ft.TextField(label="Digite o valor que deseja sacar", width=300, keyboard_type=ft.KeyboardType.NUMBER, on_change=be.somenteNumero)
        botaoConfirmarSaque = ft.ElevatedButton("Confirmar Saque", width=200, height=150, on_click=lambda e: print("Saque realizado"), style=self.estiloBotao)
        self.page.add(ft.Stack(controls=[ft.Container(content=ft.Row(controls=[valorSaque, botaoConfirmarSaque], alignment=ft.MainAxisAlignment.CENTER, spacing=30), alignment=ft.alignment.center, expand=True)], expand=True))

    def cadastroCliente(self):
        self.configurarJanela("Cadastro", 1000, 600)

        camposEsquerda = [self.campoUsuario, self.campoNome, self.campoEmail, self.campoCep, self.campoNumero, self.campoCidade]
        camposDireita = [self.campoSenha, self.campoCpf, self.campoTelefone, self.campoRua, self.campoBairro, self.campoUf]

        def aoSalvar(e):
            campos = {"nome": self.campoNome,"cpf": self.campoCpf,"email": self.campoEmail,"telefone": self.campoTelefone,"rua": self.campoRua,"bairro": self.campoBairro,"cidade": self.campoCidade,"uf": self.campoUf,"numero": self.campoNumero,"usuario": self.campoUsuario,"senha": self.campoSenha}

            erroEncontrado = False
            for nomeCampo, campo in campos.items():
                if campo.value.strip() == "":
                    campo.error_text = "Campo obrigatório"
                    erroEncontrado = True
                else:
                    campo.error_text = None
                campo.update()

            if erroEncontrado:
                return

            dadosCompletos = {"nome": self.campoNome.value.strip(),"cpf": self.campoCpf.value.strip(),"email": self.campoEmail.value.strip(),"telefone": self.campoTelefone.value.strip(),"cep": self.campoCep.value.strip(),"rua": self.campoRua.value.strip(),"bairro": self.campoBairro.value.strip(),"cidade": self.campoCidade.value.strip(),"uf": self.campoUf.value.strip(),"numero": self.campoNumero.value.strip(),"usuario": self.campoUsuario.value.strip(),"senha": self.campoSenha.value.strip(),"saldo": 0.0,"limiteCredito": 0.0,"limiteCreditoDiario": 0.0,"valorFatura": 0.0}

            def erroCallback(mensagem):
                if "cpf" in mensagem.lower():
                    self.campoCpf.error_text = "CPF já cadastrado"
                    self.campoCpf.update()
                elif "usuario" in mensagem.lower():
                    self.campoUsuario.error_text = "Usuário já existe"
                    self.campoUsuario.update()
                else:
                    self.campoUsuario.error_text = "Erro ao cadastrar"
                    self.campoUsuario.update()

            be.salvarCliente(dadosCompletos, lambda: self.telaLogin(), erroCallback)

        self.page.add(
            ft.Column(
                controls=[
                    ft.Row(
                        controls=[
                            ft.Column(controls=camposEsquerda, alignment=ft.MainAxisAlignment.CENTER),
                            ft.Column(controls=camposDireita, alignment=ft.MainAxisAlignment.CENTER)
                        ],
                        alignment=ft.MainAxisAlignment.CENTER,
                        spacing=30
                    ),
                    self.botoes
                ],
                horizontal_alignment=ft.CrossAxisAlignment.CENTER
            )
        )
