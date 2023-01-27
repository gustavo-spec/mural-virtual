import Pyro4

'''
Servidor distribuido
'''
@Pyro4.expose
class ServidorPyro():
    def teste(self):
        return "olá mundo"

'''
Main de teste
'''
def main():
    daemon = Pyro4.Daemon()
    uri = daemon.register(Servidor())
    
    print ("Servidor iniciado na porta ", daemon.port())
    print ("Objeto ", uri)
    
    daemon.requestLoop()

if __name__=="__main__":
    main()