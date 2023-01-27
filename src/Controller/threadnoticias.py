import threading
import time

'''
Classe que modifica a notícia exibida na interface gráfica;
É necessário que seja uma thread pelo fato de que a interface gráfica é un looping
'''
class ThreadNoticias(threading.Thread):
    '''
    _Constructor:
    threadId -> identificador da thread, apenas para o controle de execução
    gui -> interface gráfica recebida pelo servidor (essa thread modifica as notícias dessa interface gráfica)
    tempoExibicao -> tempo que cada notícia será exibida no sistema (padrão vindo do servidor)
    '''
    def __init__(self, threadId, gui, tempoExibicao):
        # Construtor do pai - threading
        threading.Thread.__init__(self)
        self.threadId = threadId
        self.gui = gui
        # Tempo padrão para as notícias serem exibidas
        self.tempoExibicao = tempoExibicao
        # lista de noticias que será modificado na interface gráfica
        self.noticias = []
        self.allDone = 1
    
    '''
    Altera toda a lista de noticias
    '''
    def setNoticiasSite(self, noticias):
        self.noticias = noticias
    
    '''
    Adiciona uma nova noticia na lista
    '''
    def addNoticiaSite(self, noticia):
        self.noticias.append(noticia)
    
    '''
    Remove uma notícia da lista
    '''
    def rmNoticiaSite(self, noticia):
        self.noticias.pop(noticia)
    
    '''
    Altera o tempo padrão de exibição das notícias
    '''
    def setTempoExibicao(self, tempoExibicao):
        self.tempoExibicao = tempoExibicao
    
    '''
    Sobreescrita da função da threding
    '''
    def run(self):
        while(self.allDone):
            for noticia in self.noticias:
                if self.allDone == 1:
                    # Altera na interface gráfica a notícia que está sendo exibida
                    self.gui.setNoticia(noticia)
                    # Pausa na thread para a notícia ficar o tempo em exibição
                    time.sleep(self.tempoExibicao)
                else:
                    return
    
    '''
    Função que enterrompe a execução da thread
    '''
    def stop(self):
        self.allDone = 0