from Vetor import Vetor
import Operacoes
class Luz_Spot:
    def __init__(self, posicao, intensidade, direcao, abertura,tipo):
        self.posicao = posicao
        self.intensidade = intensidade
        self.direcao = Operacoes.NormalizaVetor(direcao)
        self.abertura = abertura
        self.tipo = tipo
        return
    
    def mundoParaCamera(self, matriz):
        self.posicao = Operacoes.mult_matriz_ponto(matriz, self.posicao)
        self.direcao = Operacoes.NormalizaVetor(Operacoes.mult_matriz_vetor(matriz, self.direcao))