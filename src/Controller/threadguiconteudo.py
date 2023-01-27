from View.guiconteudo import GuiConteudo
import threading
from tkinter import *

'''
Classe que inicia a interface gráfica que exibirá os conteúdos e notícias
Ela é necessário pelo fato de que a interface gráfica é um loop, e o servidor precisa continuar em funcionamento
'''
class ThreadGuiConteudo(threading.Thread):
    '''
    _Constructor:
    threadId -> identificador da thread, apenas para o controle de execução
    '''
    def __init__(self, threadID):
        # Construtor do pai - threading
        threading.Thread.__init__(self)
        self.threadID = threadID
        # Atribui nada porque se instanciar agora, o loop da interface gráfica começa
        self.guiConteudo = None
    
    '''
    Altera a notícia que está sendo exibida;
    Essa função é utilaza na threadNoticia
    '''
    def setNoticia(self, noticia):
        self.guiConteudo.setNoticia(noticia)
    
    '''
    Altera o conteúdo que está sendo exibido;
    Essa função é utilaza na threadConteudoCentral
    '''
    def setArquivo(self, arquivo):
        self.guiConteudo.setArquivo(arquivo)
    
    '''
    Sobreescrita da função da threding
    '''
    def run(self):
        # Instancia a interface gráfica
        self.root = Tk()
        self.guiConteudo = GuiConteudo(self.root)
        self.root.mainloop()
    
    '''
    Função que enterrompe a execução
    '''
    def stop(self):
        self.guiConteudo.stop()