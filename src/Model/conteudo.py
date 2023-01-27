from datetime import date

'''
Classe que modela os conteúdos, tanto os arquivos adicionados qaunto os editais criados
Ela é abstrata
'''
class Conteudo:
    '''
    _Constructor
    codId -> vindo do banco de dados
    titulo -> nome opicional para o contepudo
    dataValidade -> data em que será retirado do sistema
    tempoExibição -> Tempo que o conteúdo será exibido
    '''
    def __subclasscheck__(self, codId, titulo, dataValidade, tempoExibicao):
        self.codId = codId
        self.titulo = titulo
        self.data = date.today()
        self.dataValidade = dataValidade
        self.tempoExibicao = tempoExibicao
    
    '''
    Getters
    '''
    def getCodId(self):
        return self.codId
    
    def getTitulo(self):
        return self.titulo
    
    def getData(self):
        return self.data
    
    def getDateValidade(self):
        return self.dataValidade
    
    '''
    Setters
    '''
    def setTitulo(self, titulo):
        self.titulo = titulo
    
    def setDataValidade(self, dataValidade):
        self.dataValidade = dataValidade