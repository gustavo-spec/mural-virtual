from Model.edital import Edital
from tkinter import *

'''
Classe cria os componentes da interface gráfica do usuário;
Ela deve disponibilizar as configurações e vizualização do sistema;
Além de configurar, adicionar e remover os conteudos e notícias;
'''
class GuiUsuario:
    '''
    _Constructor:
    Master -> classe tk() recebida por parâmetro da thread; Ela é a janela;
    '''
    def __init__(self, master, servidor):
        # Criação da janela com a api do tkinter
        self.root = master
        self.servidor = servidor
        self.root.title("Mural Virtual")
        # Deixa o sistema maximizado
        # self.root.geometry('%dx%d+0+0' % (self.root.winfo_screenwidth(), self.root.winfo_screenheight()))
        
        # Configurações padrões
        self.fontePadrao = ("Arial", "15")
        
        # Constroe o primeiro frame
        self.frameLogin()
    
    '''
    Função que constroe a primeira tela do sistema: o login
    '''
    def frameLogin(self):
        # Conteiner principal que é a tela de login inteira
        self.frameLogin = Frame(self.root)
        self.frameLogin["pady"] = 20
        self.frameLogin["border"] = 20
        self.frameLogin.pack()
        
        # Conteiner com o título do sistema e um texto informacional
        frameTitulo = Frame(self.frameLogin)
        frameTitulo["pady"] = 10
        frameTitulo.pack()
        # Titulo
        self.criaLabel(frameTitulo, "Mural Virtual", ("Ariel", "40", "bold"))
        # texto informacional
        self.criaLabel(frameTitulo, "Sistema para controle das informações do mural escolar", ("Ariel", "15", "italic"))
  
        # Conteiner para o label e input do suap para efetuação do login
        frameInfo = Frame(self.frameLogin)
        frameInfo["pady"] = 20
        frameInfo.pack()
        # Label
        self.criaLabel(frameInfo, "Efetue o login para ter acesso às configurações do conteúdo", ("Ariel", "10", "italic"))
  
        # Conteiner para o label e input do suap para efetuação do login
        frameSuap = Frame(self.frameLogin)
        frameSuap["pady"] = 20
        frameSuap.pack()
        # Label
        self.nomeLabel = Label(frameSuap, text="Suap", font=self.fontePadrao)
        self.nomeLabel.pack(side=LEFT)
        # Imput
        self.inputSuap = Entry(frameSuap)
        self.inputSuap["width"] = 30
        self.inputSuap["font"] = self.fontePadrao
        self.inputSuap.pack(side=LEFT)
        
        # Conteiner para o label e input com a senha
        frameSenha = Frame(self.frameLogin)
        frameSenha["padx"] = 20
        frameSenha.pack()
        # Label
        self.labelSenha = Label(frameSenha, text="Senha", font=self.fontePadrao)
        self.labelSenha.pack(side=LEFT)
        # Input
        self.inputSenha = Entry(frameSenha)
        self.inputSenha["width"] = 30
        self.inputSenha["font"] = self.fontePadrao
        self.inputSenha["show"] = "*"
        self.inputSenha.pack(side=LEFT)
  
        # Conteiner com o botão para efetuar o login
        frameBotaoLogin = Frame(self.frameLogin)
        frameBotaoLogin["pady"] = 20
        frameBotaoLogin.pack()
        # Botao
        self.criaButton(frameBotaoLogin, "Logar", self.buscaUsuario, ("Ariel", "10"), 20)
        
        # Conteiner com o título do sistema e um texto informacional
        frameRodape = Frame(self.frameLogin)
        frameRodape["pady"] = 2
        frameRodape.pack()
        # texto informacional
        self.criaLabel(frameRodape, "Sistema desenvolvido por: Gustavo Ribeiro, Lucas varella e Matheus Felipe", ("Ariel", "10", "italic"))

        self.mensagem = Label(frameRodape, text="", font=self.fontePadrao)
        self.mensagem.pack()
    
    '''
    Função que pega o texto dos inputs do login e valida-os
    '''
    def buscaUsuario(self):
        usuario = self.inputSuap.get()
        senha = self.inputSenha.get()
        if usuario == "" and senha == "":
            self.frameLogin.pack_forget()
            self.frameInicio()
        else:
            self.mensagem["text"] = "usuário ou senha incorreto"
    
    '''
    Função que controe a segunda tela: a de configuração dos conteúos e notícias
    '''
    def frameInicio(self):
        # Frame principal
        self.frameInicio = Frame(self.root)
        self.frameInicio.pack()
        
        # Frame com as configurações do servidor
        frameServidor = self.criaFrame(self.frameInicio, None, None, 20)
        self.criaLabel(frameServidor, "Servidor:", None, None, "L")
        self.buttonServidor = self.criaButton(frameServidor, "Iniciar", self.funcaoButtonServidor, None, None, "L")
        
        # Configuração do conteúdo
        frameEsquerda = self.criaFrame(self.frameInicio, "L", 10, 10)
        self.criaLabel(frameEsquerda, "Opções para os conteúdo", None, "green")
        self.criaButton(frameEsquerda, "Adicionar conteúdo", self.addConteudoAoDiretorio)
        self.criaButton(frameEsquerda, "Criar conteúdo", self.criaConteudo)
        
        # Configuração das  notícias
        frameDireita = self.criaFrame(self.frameInicio, "R", 10, 10)
        self.criaLabel(frameDireita, "Opções para as notícias", None, "green")
        self.criaLabel(frameDireita, "Selecione abaixo quais sites deseja buscar notícias:")
        
        self.checkboxIf = Checkbutton(frameDireita, text="IFG - Campus Inhumas")
        self.checkboxIf.pack()
        
        self.checkboxG1 = Checkbutton(frameDireita, text="G1.com")
        self.checkboxG1.pack()
        
        self.checkboxGoogle = Checkbutton(frameDireita, text="Google")
        self.checkboxGoogle.pack()
        
        self.criaButton(frameDireita, "Salvar", self.salvaNoticias)
    
    '''
    Função que inicia e encerra a execção do servidor
    '''
    def funcaoButtonServidor(self):
        if self.servidor.getStatus() == 0:
            # Liga servidor
            self.servidor.iniciaServidor()
            if self.servidor.getStatus() == 1:
                self.buttonServidor["text"] = "Parar"
            else:
                self.servidor.geraLog("Ao iniciar o servidor", "guiUsuario.iniciaServidor")
        else:
            # Desliga servidor
            self.servidor.paraServidor()
            if self.servidor.getStatus() == 0:
                self.buttonServidor["text"] = "Iniciar"
            else:
                self.servidor.geraLog("Ao encerrar o servidor", "guiUsuario.funcaoButtonServidor -> encerrar")
    
    '''
    Função que salva no servidor as páginas de notícias selecionadas
    '''
    def salvaNoticias(self):
        pass
    
    '''
    Função que abre o diretório para adicionar um conteúdo ao sistema
    '''
    def addConteudoAoDiretorio(self):
        pass
    
    '''
    Função que cria a interface para criar um novo conteúdo
    '''
    def criaConteudo(self):
        # primeiro desabilita a tela anterior
        self.frameInicio.pack_forget()
        
        # frame com a edição do conteúdo
        self.frameCriaConteudo = Frame(self.root)
        self.frameCriaConteudo["pady"] = 20
        self.frameCriaConteudo["border"] = 20
        self.frameCriaConteudo.pack()
        
        # Titulo do conteudo
        frameTituloCriaConteudo = Frame(self.frameCriaConteudo)
        frameTituloCriaConteudo.pack()
        
        self.inputTitulo = Entry(frameTituloCriaConteudo)
        self.inputTitulo["width"] = 50
        self.inputTitulo.pack()
        
        # Subtitulo do conteudo
        frameSubtituloConteudo = Frame(self.frameCriaConteudo)
        frameSubtituloConteudo.pack()
        
        self.inputSubtitulo = Entry(frameSubtituloConteudo)
        self.inputSubtitulo["width"] = 50
        self.inputSubtitulo.pack()
        
        # Conteudo
        frameConteudo = Frame(self.frameCriaConteudo)
        frameConteudo.pack()
        
        self.textConteudo = Text(frameConteudo)
        self.textConteudo["width"] = 50
        self.textConteudo.pack()
        
        # Botão para voltar
        self.criaButton(frameConteudo, "Voltar", self.voltaInicio, None, None, "L")
        
        # Botão para criar o conteúdo
        self.criaButton(frameConteudo, "Salvar", self.salvaConteudoCriado, None, None, "R")
    
    '''
    Função que salva o conteúdo criado na função de criaConteudo
    '''
    def salvaConteudoCriado(self):
        if len(self.textConteudo.get(1.0, END)) == 1:
            Alerta("por favor, informe o conteúdo.\nEsse campo é onrigatório")
        else:
            edital = Edital(None, self.inputTitulo.get(), self.inputSubtitulo.get(), self.textConteudo.get(1.0, END))
            Alerta("Salvo com sucesso!")
    
    '''
    Função que volta para a tela anterior
    '''
    def voltaInicio(self):
        self.frameCriaConteudo.pack_forget()
        self.frameInicio.pack()
    
    '''
    Função que cria um frame
    '''
    def criaFrame(self, frameRoot, lado=None, pady=None, border=None):
        frame = Frame(frameRoot)
        if pady != None:
            frame["pady"] = pady
        if border != None:
            frame["border"] = border
        if lado != None:
            if lado == "L":
                frame.pack(side=LEFT)
            if lado == "R":
                frame.pack(side=RIGHT)
            if lado != "R" or lado != "L":
                frame.pack()
        else:
            frame.pack()
        return frame
    
    '''
    Função que cria um label automaticamente - Para diminuir a quantidade de código
    frame -> o frame que o label será adiciona
    texto -> O texto do label
    color -> cor personalizada de background (opcional)
    font -> fonte personalizada (opcional)
    lado -> posição em que ficará: L = esquerda; R = direita
    '''
    def criaLabel(self, frame, texto, font=None, color=None, lado=None):
        label = Label(frame, text=texto)
        if color != None:
            label["bg"] = color
        if font != None:
            label["font"] = font
        if lado != None:
            if lado == "L":
                label.pack(side=LEFT)
            if lado == "R":
                label.pack(side=RIGHT)
            if lado != "R" or lado != "L":
                label.pack()
        else:
            label.pack()
    
    '''
    Função que cria um botão automaticamente - Para diminuir a quantidade de código
    frame -> frame que o botão será adicionado
    texto -> o texto do botão
    font -> fonte para o texto personalizado
    width -> tamanho do botão
    lado -> posição em que ficará: L = esquerda; R = direita
    '''
    def criaButton(self, frame, texto, command, font=None, width=None, lado=None):
        button = Button(frame)
        button["text"] = texto
        button["command"] = command
        if font != None:
            button["font"] = font
        if width != None:
            button["width"] = width
        if lado != None:
            if lado == "L":
                button.pack(side=LEFT)
            if lado == "R":
                button.pack(side=RIGHT)
            if lado != "R" or lado != "L":
                button.pack()
        else:
            button.pack()
        return button

'''
Classe que cria uma janela para exibir informações e alertas para o usuário
'''
class Alerta:
    '''
    _Constructor:
    texto -> texto que será exibido na tela
    '''
    def __init__(self, texto):
        self.root = Tk()
        self.root.title("Info")
        
        # Formatação do tamanho da tela
        self.root.geometry('%dx%d+0+0' % (self.root.winfo_screenwidth() * 0.3, self.root.winfo_screenheight() * 0.15))
        
        texto = texto + "\n\n"
        
        label = Label(self.root, text=texto)
        label.pack()
        button = Button(self.root, text="Continuar", command=self.exit)
        button.pack()
    
    '''
    Função para fechar a tela ao clicar no botão
    '''
    def exit(self):
        self.root.destroy()