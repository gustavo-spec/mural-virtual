from View.guiusuario import GuiUsuario
import threading
from tkinter import *

'''
Classe que inicia a interface gráfica com as configurações e ações que o usuário poderá fazer
Ela é necessário pelo fato de que a interface gráfica é um loop, e o servidor precisa continuar em funcionamento
'''
class ThreadGuiUsuario(threading.Thread):
    '''
    _Constructor:
    threadId -> identificador da thread, apenas para o controle de execução
    '''
    def __init__(self, threadID, servidor):
        # Construtor do pai - threading
        threading.Thread.__init__(self)
        self.threadID = threadID
        self.servidor = servidor
        # Atribui nada porque se instanciar agora, o loop da interface gráfica começa
        self.guiUsuario = None
    
    '''
    Sobreescrita da função da threding
    '''
    def run(self):
        # Instancia a interface gráfica
        self.root = Tk()
        self.guiUsuario = GuiUsuario(self.root, self.servidor)
        self.root.mainloop()
    
    '''
    Função que enterrompe a executação
    '''
    def stop(self):
        self.root.destroy()