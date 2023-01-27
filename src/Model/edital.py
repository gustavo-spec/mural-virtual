from Model.conteudo import Conteudo

'''
Classe que modela as informações, editais e conteúdos criados pelo sistema
'''
class Edital (Conteudo):
    '''
    _Constructor:
    subtitulo -> definido pelo usuário (opcional)
    conteudo -> texto, informação, etc...
    '''
    def __init__(self, codId, titulo, dataValidade, tempoExibicao, subtitulo, conteudo):
        Model.Conteudo.__subclasscheck__(self, codId, titulo, dataValidade, tempoExibicao)
        self.subtitulo = subtitulo
        self.conteudo = conteudo
    
    '''
    Getters
    '''
    def getSubtitulo(self):
        return self.subtitulo
    
    def getConteudo(self):
        return self.conteudo
    
    '''
    Setters
    '''
    def setSubtitulo(self, subtitulo):
        self.subtitulo = subtitulo
    
    def setConteudo(self, conteudo):
        self.conteudo = conteudo