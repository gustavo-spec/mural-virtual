from PIL import Image
from tkinter import *

class GuiConteudo:
    def __init__(self, master):
        # Criação da janela com a api do tkinter
        self.root = master
        self.root["bg"] = "white"
        self.root.title("Mural Virtual")
        # Deixa o programa em tela cheia
        #self.root.attributes('-fullscreen', True)
        self.root.geometry('%dx%d+0+0' % (self.root.winfo_screenwidth(), self.root.winfo_screenheight() * 0.2))
        
        # Chamada da função que cria o conteúdo central
        self.conteudoCentral()
        
        # Chamada da função que cria as notícias no rodapé
        self.areaDasNoticias()
    
    def conteudoCentral(self):
        # Conteiner principal
        self.frameConteudoCentral = Frame(self.root)
        self.frameConteudoCentral.pack()
        
        self.labelConteudo = Label(self.frameConteudoCentral)
        self.labelConteudo.pack()
    
    def setArquivo(self, arquivo):
        img = PhotoImage(Image.open(arquivo))
        self.labelConteudo.image = img
    
    def areaDasNoticias(self):
        # Conteiner em que passará as notícias do portal
        self.frameNoticias = Frame(self.root)
        self.frameNoticias.pack()
        
        # Label com as noticias
        self.labelNoticia = Label(self.frameNoticias, text="Noticia", font=("Arial", "15"))
        self.labelNoticia["bg"] = "blue"
        self.labelNoticia.pack(side=LEFT, fill=Y)
    
    def setNoticia(self, noticia):
        self.labelNoticia["text"] = noticia
    
    def stop(self):
        self.root.destroy()