from Operacoes import ProdutoVetorial
from Operacoes import Subtracao_vetores
from Operacoes import NormalizaVetor
from Operacoes import mult_matriz_ponto
from Plano import Plano
from Vetor import Vetor
class Face:
    def __init__(self,ponto1,ponto2,ponto3):
        self.ponto1 = ponto1
        self.ponto2 = ponto2
        self.ponto3 = ponto3
        p1p2 = Subtracao_vetores(ponto1,ponto2)
        p1p3 = Subtracao_vetores(ponto1,ponto3)
        self.normal=NormalizaVetor(ProdutoVetorial(p1p2,p1p3))
        self.plano = Plano(ponto1,self.normal,Vetor(0,0,0),1,"plano")
        
        return
    
    def Calcular_Normal(self):
        return self.normal
    
    def mundoParaCamera(self, matriz):
        self.ponto1 = mult_matriz_ponto(matriz, self.ponto1)
        self.ponto2 = mult_matriz_ponto(matriz, self.ponto2)
        self.ponto3 = mult_matriz_ponto(matriz, self.ponto3)