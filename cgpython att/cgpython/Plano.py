from Raio import Raio
import Operacoes
import math
class Plano:
    def __init__(self, p_pi, n_bar, material, m, tipo):
        self.tipo = tipo
        self.p_pi = p_pi
        self.n_bar = Operacoes.NormalizaVetor(n_bar)
        self.material = material
        self.m = m
        return
    
    def IntercecaoPlano(self,raio):
        
         w = Operacoes.Subtracao_vetores(self.p_pi,raio.Origem)
   
         numerador   = Operacoes.ProdutoEscalar(w, self.n_bar)
         denominador = Operacoes.ProdutoEscalar(raio.Direcao, self.n_bar)
    
         if(denominador == 0 ):
             return math.inf
         t_i = numerador/denominador
         if(t_i < 0):
             pt1 = math.inf
         else:
             pt1 = Operacoes.EquacaoReta(t_i,raio)
         
    
         return pt1
     
    def Calcular_Normal(self, t):
        return self.n_bar
    
    def mundoParaCamera(self, matriz):
        self.p_pi = Operacoes.mult_matriz_ponto(matriz, self.p_pi)
        self.n_bar = Operacoes.NormalizaVetor(Operacoes.mult_matriz_vetor(matriz, self.n_bar))