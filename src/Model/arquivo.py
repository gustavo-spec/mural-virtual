from Model.conteudo import Conteudo
import os

'''
Classe para a modelagem do conteudo. Esse conteudo é o conteúdo adicionado pelo usuário
'''
class Arquivo (Conteudo):
    '''
    _Constructor:
    nomeOriginal -> nome original do arquivo no diretório recebido pelo servidor
    url -> caminho da pasta que estará os arquivos do sistema
    descricao -> descrição dada pelo usuário para definir o que é o conteúdo - (opcional)
    '''
    def __init__(self, codId, titulo, dataValidade, tempoExibicao, nomeOriginal, url, descricao=None):
        Conteudo.__subclasscheck__(self, codId, titulo, dataValidade, tempoExibicao)
        self.formato = None
        self.nomeArquivo = None
        self.url = url + "Conteudos/"
        self.descricao = descricao
        # Chamada da função que renomeia o arquivo
        self.mudaNome(nomeOriginal)
    
    '''
    O formato do arquivo talvez será padrão, porém é possivel alterar.
    O diretório do arquivo poderá ser alterado atraves de um input futuramente
    Parametos: nomeOriginal -> nome do arquivo no diretorio. Esse parametro é recebido da classe servidor
    '''
    def mudaNome(self, nomeOriginal):
        # Separa o nome do arquivo em várias posições em uma lista
        dados = str(nomeOriginal).split(".")
        # Pega a última posição do dados; ela contem o formato do arquivo
        self.formato = dados[len(dados) - 1]
        # cria o novo nome para o arquivo
        self.nomeArquivo = ("%s_%s.%s") % (str(self.codId), str(self.data), str(self.formato))
        # Renomeia o arquivo
        os.rename(self.url + nomeOriginal, self.url + self.nomeArquivo)
        
    '''
    Getters
    '''
    def getNomeArquivo(self):
        return self.nomeArquivo
    
    def getUrl(self):
        return self.url
    
    def getFormato(self):
        return self.formato
    
    def getDescricao(self):
        return self.descricao
    
    '''
    Setters
    '''
    def setDescricao(self, descricao):
        self.descricao = descricao