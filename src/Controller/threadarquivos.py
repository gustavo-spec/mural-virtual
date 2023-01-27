import threading
import time

'''
Classe que modifica o conteúdo central do sistema na interface gráfica;
É necessário que seja uma thread pelo fato de que a interface gráfica é un looping
'''
class ThreadArquivos (threading.Thread):
    '''
    _Constructor:
    threadId -> identificador da thread, apenas para o controle de execução
    gui -> interface gráfica recebida pelo servidor (essa thread modifica os conteúdos dessa interface gráfica)
    
    obs.: Não é necessário um tempo de exibição como na classe da notícia;
    O conteúdo já tem esse tempo de exibição
    '''
    def __init__(self, threadId, gui):
        # Construtor do pai - threading
        threading.Thread.__init__(self)
        self.threadId = threadId
        self.gui = gui
        # lista de arquivos que será modificado na interface gráfica
        self.arquivos = []
        self.allDone = 1
    
    '''
    Altera toda a lista de arquivos
    '''
    def setAquivos(self, arquivos):
        self.arquivos = arquivos
    
    '''
    Adiciona um novo conteúdo à lista
    '''
    def addArquivo(self, arquivo):
        self.arquivos.append(arquivo)
    
    '''
    Remove um arquivo da lista
    '''
    def rmArquivo(self, arquivo):
        self.arquivos.pop(arquivo)
    
    '''
    Sobreescrita da função da threding
    '''
    def run(self):
        while(self.allDone):
            for arquivo in self.arquivos:
                if self.allDone == 1:
                    # Altera o conteúdo na interface gráfica
                    self.gui.setArquivo(arquivo.getUrl() + arquivo.getNomeArquivo())
                    # Pausa na thread para o conteúdo ficar o tempo em exibição
                    time.sleep(arquivo.getTempoExibicao())
                else:
                    return
    
    '''
    Função que enterrompe a execução da thread
    '''
    def stop(self):
        self.allDone = 0