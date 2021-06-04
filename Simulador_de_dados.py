#Simular um jogo de dados sorteando um número aleatório utilizando a biblioteca random.
import random 

class SimuladorDeDados:
    # O método __init__ serve para fazermos as configurações iniciais do Objeto.
    def __init__(self): 
        self.valor_minimo = 1
        self.valor_maximo = 6
        self.mensagem = 'Você gostaria de gerar um novo valo? '
    
    def Iniciar(self):
        resposta = input(self.mensagem).upper()
        try:
            if resposta == 'SIM':
                #fazendo um método o código fica organizado e facilita na hora de fazer manutenções.
                self.gerarvalordedado()
            
            elif resposta == 'NÃO':
                print('Agradecemos sua participação')
            else:
                print('Por favor, digite sim ou não')
        except:
            print('Ops! Houve um erro de comunicação')


    def gerarvalordedado(self):
        print(random.randint(self.valor_minimo, self.valor_maximo))

simulador = SimuladorDeDados()
simulador.Iniciar()