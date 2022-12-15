from Vetor import Vetor
import Operacoes
class Luz_Direcional:
    def __init__(self, direcao, intensidade,tipo):
        self.direcao = direcao
        self.intensidade = intensidade
        self.tipo = tipo
        return

    def mundoParaCamera(self, matriz):
        self.posicao = Operacoes.mult_matriz_ponto(matriz, self.posicao)