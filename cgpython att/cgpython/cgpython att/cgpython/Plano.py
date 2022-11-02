from Raio import Raio
import Operacoes
import math
class Plano:
    def __init__(self, p_pi, n_bar, material, m, tipo):
        self.tipo = tipo
        self.p_pi = p_pi
        self.n_bar = n_bar
        self.material = material
        self.m = m
        return
    
    def IntercecaoPlano(self,raio):
         w = Operacoes.Subtracao_vetores(raio.Origem, self.p_pi )
   
         numerador   = Operacoes.ProdutoEscalar(w, self.p_pi)
         denominador = Operacoes.ProdutoEscalar(raio.Direcao, self.p_pi)
    
         if(denominador == 0 ):
             return math.inf
         t_i = -numerador/denominador
         if(t_i < 0):
             pt1 = math.inf
         else:
             pt1 = Operacoes.EquacaoReta(t_i,raio)
         
    
         return pt1
     
    def Calcular_Normal(self, t):
        return self.n_bar