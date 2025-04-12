import flet as ft
import backend.backend as be

class Tela:
    def __init__(self, page: ft.Page):
        self.page = page

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

        campoUsuario = ft.TextField(
            label="Digite o nome do usuário",
            on_change=be.tirarErro,
            prefix_icon=ft.icons.PERSON,
            capitalization=ft.TextCapitalization.CHARACTERS,
            width=300
        )

        campoSenha = ft.TextField(
            label="Digite a senha",
            on_change=be.tirarErro,
            password=True,
            can_reveal_password=True,
            width=300,
            prefix_icon=ft.icons.LOCK_PERSON_OUTLINED
        )

        botaoEntrar = ft.ElevatedButton(
            "Entrar",
            width=300,
            on_click=lambda e: be.verificarValoresInput(self.page, campoUsuario, campoSenha, self.paginaInicial)
        )

        botaoCadastrar = ft.ElevatedButton(
            "Cadastrar",
            width=300,
            on_click=lambda e: self.cadastroCliente()
        )

        conteudo = ft.Container(
            content=ft.Column(
                controls=[campoUsuario, campoSenha, botaoEntrar, botaoCadastrar],
                alignment=ft.MainAxisAlignment.CENTER,
                horizontal_alignment=ft.CrossAxisAlignment.CENTER
            )
        )

        self.page.add(conteudo)

    def paginaInicial(self):
        self.configurarJanela("Bem-vindo", 1000, 600)

        modoEscuro = self.page.platform_brightness.value == "dark"
        corFundo = ft.colors.WHITE if modoEscuro else ft.colors.BLACK
        corTexto = ft.colors.BLACK if modoEscuro else ft.colors.WHITE

        botaoSair = ft.ElevatedButton(
            text="Sair",
            icon=ft.icons.ARROW_BACK,
            bgcolor=corFundo,
            color=corTexto,
            on_click=lambda e: self.telaLogin()
        )

        estiloBotao = ft.ButtonStyle(
            bgcolor=corFundo,
            color=corTexto,
            shape=ft.RoundedRectangleBorder(radius=75),
            padding=20,
            text_style=ft.TextStyle(weight=ft.FontWeight.BOLD, size=26)
        )

        botaoSacar = ft.ElevatedButton("SACAR", width=200, height=150, on_click=lambda e: None, style=estiloBotao)
        botaoDepositar = ft.ElevatedButton("DEPOSITAR", width=200, height=150, on_click=lambda e: None, style=estiloBotao)
        botaoTransferir = ft.ElevatedButton("TRANSFERIR", width=200, height=150, on_click=lambda e: None, style=estiloBotao)

        self.page.add(
            ft.Container(content=botaoSair, alignment=ft.alignment.top_left, padding=10),
            ft.Stack(
                controls=[
                    ft.Container(
                        content=ft.Row(
                            controls=[botaoSacar, botaoDepositar, botaoTransferir],
                            alignment=ft.MainAxisAlignment.CENTER,
                            spacing=30
                        ),
                        alignment=ft.alignment.center,
                        expand=True
                    )
                ],
                expand=True
            )
        )

    def cadastroCliente(self):

        self.configurarJanela("Cadastro", 1000, 600)

        campoRua = ft.TextField(label="Rua", width=300, capitalization=ft.TextCapitalization.CHARACTERS)
        campoBairro = ft.TextField(label="Bairro", width=300, capitalization=ft.TextCapitalization.CHARACTERS)
        campoCidade = ft.TextField(label="Cidade", width=300, capitalization=ft.TextCapitalization.CHARACTERS)
        campoUf = ft.TextField(label="UF", width=300, capitalization=ft.TextCapitalization.CHARACTERS)

        campoUsuario = ft.TextField(label="Usuário", width=300, capitalization=ft.TextCapitalization.CHARACTERS)
        campoSenha = ft.TextField(label="Senha", width=300, password=True, can_reveal_password=True)

        campoNome = ft.TextField(label="Nome", width=300, capitalization=ft.TextCapitalization.WORDS, on_change=be.formatarNome)
        campoEmail = ft.TextField(label="Email", width=300, keyboard_type=ft.KeyboardType.EMAIL, on_change=be.validarEmail)
        campoCep = ft.TextField(label="CEP", width=300, keyboard_type=ft.KeyboardType.NUMBER, on_change=lambda e: be.validarCep(e, campoRua, campoBairro, campoCidade, campoUf))
        campoNumero = ft.TextField(label="Número", width=300, keyboard_type=ft.KeyboardType.NUMBER, on_change=be.somenteNumero)
        campoCpf = ft.TextField(label="CPF", width=300, keyboard_type=ft.KeyboardType.NUMBER, on_change=be.validarCpf)
        campoTelefone = ft.TextField(label="Telefone", width=300, keyboard_type=ft.KeyboardType.NUMBER, on_change=be.formatarTelefone)

        camposEsquerda = [campoUsuario, campoNome, campoEmail, campoCep, campoNumero, campoCidade]
        camposDireita = [campoSenha, campoCpf, campoTelefone, campoRua, campoBairro, campoUf]

        def aoSalvar(e):
            campos = {
                "nome": campoNome,
                "cpf": campoCpf,
                "email": campoEmail,
                "telefone": campoTelefone,
                "rua": campoRua,
                "bairro": campoBairro,
                "cidade": campoCidade,
                "uf": campoUf,
                "numero": campoNumero,
                "usuario": campoUsuario,
                "senha": campoSenha
            }

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

            dadosCompletos = {
                "nome": campoNome.value.strip(),
                "cpf": campoCpf.value.strip(),
                "email": campoEmail.value.strip(),
                "telefone": campoTelefone.value.strip(),
                "cep": campoCep.value.strip(),
                "rua": campoRua.value.strip(),
                "bairro": campoBairro.value.strip(),
                "cidade": campoCidade.value.strip(),
                "uf": campoUf.value.strip(),
                "numero": campoNumero.value.strip(),
                "usuario": campoUsuario.value.strip(),
                "senha": campoSenha.value.strip(),
                "saldo": 0.0,
                "limiteCredito": 0.0,
                "limiteCreditoDiario": 0.0,
                "valorFatura": 0.0
            }

            def erroCallback(mensagem):
                if "cpf" in mensagem.lower():
                    campoCpf.error_text = "CPF já cadastrado"
                    campoCpf.update()
                elif "usuario" in mensagem.lower():
                    campoUsuario.error_text = "Usuário já existe"
                    campoUsuario.update()
                else:
                    campoUsuario.error_text = "Erro ao cadastrar"
                    campoUsuario.update()

            be.salvarCliente(dadosCompletos, lambda: self.telaLogin(), erroCallback)



        botoes = ft.Row(
            controls=[
                ft.ElevatedButton("Voltar", width=300, on_click=lambda e: self.telaLogin()),
                ft.ElevatedButton("Salvar", width=300, on_click=aoSalvar)
            ],
            alignment=ft.MainAxisAlignment.CENTER,
            spacing=30
        )

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
                    botoes
                ],
                horizontal_alignment=ft.CrossAxisAlignment.CENTER
            )
        )
