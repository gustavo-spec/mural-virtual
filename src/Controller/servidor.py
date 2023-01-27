from Controller.threadarquivos import ThreadArquivos
from Controller.threadguiconteudo import ThreadGuiConteudo
from Controller.threadguiusuario import ThreadGuiUsuario
from Controller.threadnoticias import ThreadNoticias
from Model.arquivo import Arquivo
from bs4 import BeautifulSoup
from datetime import date
import os
import requests
import time

'''
Classe que faz o controle das aplicações e inicia todas as funcionalidades do sistema;
Ela deve inciar todas as threads que vão rodar e fazer o controle de execução
'''
class Servidor:
    '''
    _Contructor:
    '''
    def __init__(self):
        # Antes de qualquer coisa, o sistema deve realizar a configuração do sistema para rodar a aplicação
        # Configura as url e diretorios do programa
        self.url = os.path.expanduser("~/MuralVirtual/") # busca o usuario logado na máquina
        self.configDiretorio() # Configura os diretórios
        self.status = 0 # Status 0 -> offiline
        
        # Cria as variáveis que são utilizadas
        self.threadGuiUsuario = None # Thread da interface gráfica do usuario
        self.threadGuiConteudo = None # Thread da interface gráfica do conteudo
        self.threadArquivos = None # Thread que muda o conteúdo central
        self.sites = [] # Lista de sites que serão buscadas asa notícias
        self.threadNoticias = None # Thread que muda as notícias
        
        # A primeira coisa que o sistema deve fazer é iniciar a parte do usuário;
        # Ele adiciona, cria, edita, inicia e finaliza a exibição dos conteúdos;
        # ID -> 1
        self.threadGuiUsuario = ThreadGuiUsuario(1, self)
        self.threadGuiUsuario.start()
    
    '''
    Adiciona um conteudo na lista para ser exibido
    '''
    def addArquivo(self, arquivo):
        self.threadArquivos.addArquivo(arquivo)
    
    '''
    Remove um conteudo da lista
    '''
    def rmArquivo(self, arquivo):
        self.threadArquivos.rmArquivo(arquivo)
    
    '''
    Adiciona um site para fazer requisição
    '''
    def addSiteDeNoticias(self, url):
        self.sites.append(url)
    
    '''
    Remove um site da lista de requisições
    '''
    def rmSiteDeNoticias(self):
        self.sites.pop(url)
        
    '''
    Função que verifica se a pasta para guardar as imagens já existe, e caso não exista, cria uma
    '''
    def configDiretorio(self):
        # Verifica se a pasta do MuralVirtual existe
        if os.path.isdir(self.url):
            # Verifica se a pasta para o historico existe
            existeH = 0 # 0 -> Não existe
            if os.path.isdir(self.url + "Historico"):
                existeH = 1 # 1 -> Existe
            if existeH == 0:
                os.mkdir(self.url + "Historico")
            
            # Verifica se a pasta para o Conteudo existe
            existeC = 0 # 0 -> Não existe
            if os.path.isdir(self.url + "Conteudos"):
                existeC = 1 # 1 -> Existe
            if existeC == 0:
                os.mkdir(self.url + "Conteudos")
                
            # Verifica se a pasta dos logs existe
            existeL = 0 # 0 -> Não existe
            if os.path.isdir(self.url + "Logs"):
                existeL = 1 # 1 -> existe
            if existeL == 0:
                os.mkdir(self.url + "Logs")
        else:
            '''
            Se a pasta do Mural Virtual não existe, cria-se
            Dentro da pasta do MuralVirtual existem outras 3 pastas:
            Historico -> Contem os arquivos removidos que não serão mais exibidos
            Conteudos -> Os arquivos que ainda são exibidos
            Logs -> Os erros que podem ocorrer no sistema
            '''
            os.mkdir(self.url)
            os.mkdir(self.url + "Historico")
            os.mkdir(self.url + "Conteudos")
            os.mkdir(self.url + "Logs")

    '''
    Função que cria e adiciona os logs do sistema
    '''
    def geraLog(self, erro, local):
        # Nome do arquivo de log
        nome_arquivo = self.url + "Logs/" + "log_" + str(date.today()) + ".txt"
        # Abre o arquivo de log referente ao dia e caso não exista, cria o arquivo
        arquivo = open(nome_arquivo, "a")
        # Configura o log que irá para o arquivo
        texto = "Hora: " + time.strftime("%H:%M:%S") + "\nErro: " + erro + "\nLocal: " + local
        # Adiciona o texto do log no arquivo de log
        arquivo.write(texto + "\n\n")

    '''
    Função que inicia a exibição dos conteudos
    Ela cria a instancia da interface gráfica que é uma thread
    '''
    def iniciaServidor(self):
        # Inicia a parte gráfica
        self.threadGuiConteudo = ThreadGuiConteudo(2)
        self.threadGuiConteudo.start()
        
        # A função buscaConteudos é chamada primeiro;
        # logo, assim que a interface gráfica iniciar, iniciará também as outras threads;
        # As outras threads mudam os conteudos e as notícias que estão sendo exibidos
        self.threadArquivos = ThreadArquivos(3, self.threadGuiConteudo)
        self.threadArquivos.start()
        
        self.threadNoticias = ThreadNoticias(4, self.threadGuiConteudo, 2)
        self.threadNoticias.start()
        
        # Busca os conteúdos que estão no sistema
        self.leDiretorio()
        
        # teste
        self.sites.append('https://www.ifg.edu.br/inhumas')
        self.sites.append('https://g1.globo.com/')
        self.sites.append('https://news.google.com/?hl=pt-BR&gl=BR&ceid=BR:pt-419')
        
        # Busca as notícias de sites
        # Se a url estiver na lista, chamará a função referente a ela para buscar as notícias
        for url in self.sites:
            if url == 'https://www.ifg.edu.br/inhumas':
                self.requisicoesSiteIF()
            if url == 'https://g1.globo.com/':
                self.requisicoesSiteG1()
            if url == 'https://news.google.com/?hl=pt-BR&gl=BR&ceid=BR:pt-419':
                self.requisicoesSiteGoogle()
        
        # Altera para servidor rodando
        self.status = 1
    
    '''
    Função que interrompe o fluxo de execução
    '''
    def paraServidor(self):
        self.threadNoticias.stop()
        self.threadArquivos.stop()
        self.threadGuiConteudo.stop()
        self.status = 0
    
    '''
    Função que le os arquivos do diretorio e configura eles mandando para a thread executar
    '''
    def leDiretorio(self):
        # Leitura dos arquivos do diretorio
        codId = 0
        for nomeOriginal in os.listdir(self.url + "Conteudos/"):
            codId += 1
            arquivo = Arquivo(codId, "Nome", "28/11/2000", 2, nomeOriginal, self.url, "Descrição")
            self.addArquivo(arquivo)
    
    '''
    Função que faz conexão com o site do IFG campus inhumas e busca as notícias
    '''
    def requisicoesSiteIF(self):
        try:
            # url do site
            url = 'https://www.ifg.edu.br/inhumas'
            # requests.get retorna status de conexão com o site->200/ status_code
            pagina = requests.get(url)
            # pega as informações do site identado com o parametro 'html.parser'
            noticia = BeautifulSoup(pagina.text, 'html.parser')
            # busca o conteúdo do site de acordo com a tag, class, id, etc...
            for informacoes in noticia.find_all('h3'):
                self.threadNoticias.addNoticiaSite(informacoes.get_text().strip())
        except:
            # Criação do arquivo de log com o erro
            self.geraLog("Requisições das notícias do site do IFG", "Servidor.requisicoesSiteIF")
    
    '''
    Função que faz conexão com o site do g1 e busca as notícias
    '''
    def requisicoesSiteG1(self):
        try:
            # url do site
            url = 'https://g1.globo.com/'
            # requests.get retorna status de conexão com o site->200/ status_code
            pagina = requests.get(url)
            # pega as informações do site identado com o parametro 'html.parser'
            noticia = BeautifulSoup(pagina.text, 'html.parser')
            # usca o conteúdo do site de acordo com a tag, class, id, etc...
            for informacoes in noticia.find_all(class_='feed-post-link'):
                self.threadNoticias.addNoticiaSite(informacoes.get_text().strip())
        except:
            self.geraLog("Requisições das notícias do site do G1", "Servidor.requisicoesSiteG1")
    
    '''
    Função que faz conexão com o site do google e busca as notícias
    '''
    def requisicoesSiteGoogle(self):
        try:
            # url do site
            url = 'https://news.google.com/?hl=pt-BR&gl=BR&ceid=BR:pt-419'
            # requests.get retorna status de conexão com o site->200/ status_code
            pagina = requests.get(url)
            # pega as informações do site identado com o parametro 'html.parser'
            noticia = BeautifulSoup(pagina.text, 'html.parser')
            # busca o conteúdo do site de acordo com a tag, class, id, etc...
            for informacoes in noticia.find_all('h3'):
                self.threadNoticias.addNoticiaSite(informacoes.get_text().strip())
        except:
            self.geraLog("Requisições das notícias do site do Google", "Servidor.requisicoesSiteGoogle")
    
    '''
    Getters
    '''
    def getStatus(self):
        return self.status