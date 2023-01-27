import MySQLdb
from Model.conteudo import Conteudo

class DataBase:
    def __init__(self):
        # Gera a string de conexao ex.: seu host, seu usuario, sua senha e seu db
        db = MySQLdb.connect(host="localhost", user="root", passwd="aluno123", db="MuralVirtual")
        con.select_db('MuralVirtual')
        cursor = con.cursor()
        usuario = Cliente()
        conteudo = Conteudo()

    def buscaUsuario(self, suap):
        buscou = cursor.execute('SELECT * FROM Usuarios WHERE suap = ' + str(suap))
        if buscou:
            usuario = mycursor.fetchall()
            print (usuario)
            return usuario
        else:
            return 0

    def insereUsuario(self, usuario):
        executou = cursor.execute('INSERT INTO Usuarios (nome, suap, senha) VALUES (?,?,?)', (usuario.getNome(), usuario.getSuap(), usuario.getSenha()))
        if executou:
            con.commit()
        else:
            print ("Ocorreu um erro ao inserir um usuario no sistema, contate o administrador do mesmo!")


    def insereConteudo(self, conteudo):
        executou = cursor.execute ('INSERT INTO Conteudos (id, nome, nomeOriginal, descricao, data, dataValidade) VALUES (?,?,?,?,?,?)', (conteudo.getCodId(), conteudo.getNome(), conteudo.getNomeOriginal(), conteudo.getDescricao(), conteudo.getData(), conteudo.getDataValidade()));
        if executou:
            con.commit()
        else:
            print ("Ocorreu um erro ao inserir um conteudo no sistema, contate o administrador do mesmo!")
