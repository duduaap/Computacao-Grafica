from Vetor import Vetor
import Operacoes
class Luz_Pontual:
    def __init__(self, posicao, intensidade,tipo):
        self.posicao = posicao
        self.intensidade = intensidade
        self.tipo = tipo
        return
    
    def mundoParaCamera(self, matriz):
        self.posicao = Operacoes.mult_matriz_ponto(matriz, self.posicao)