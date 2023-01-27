'''
Classe que modela o usuário; ela é mais usada pelo banco de dados, apenas para acessar e configurar o sistema
'''
class Usuario:
    '''
    _Constructor:
    suap -> identificação do usuário no sistema
    nome -> nome do usário
    senha -> senha criada pelo usário para acessar o sistema
    '''
    def __init__(self, suap=None, nome=None, senha=None):
        self.suap = suap
        self.nome = nome
        self.senha = senha
    
    '''
    Getters
    '''
    def getNome(self):
        return self.nome
        
    def getSuap(self):
        return self.suap
    
    def getSenha(self):
        return self.senha
    
    '''
    Setters
    '''
    def setNome(self, nome):
        self.nome = nome
    
    def setSuap(self, suap):
        self.suap = suap
        
    def setSenha(self, senha):
        self.senha = senha