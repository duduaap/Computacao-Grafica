from asyncio.windows_events import NULL
import Operacoes
import numpy as np
import math

class Cilindro:
    def __init__(self,CentroBase,RaioBase,Altura,direcao,material, m,tipo):
        self.CentroBase = CentroBase
        self.RaioBase = RaioBase
        self.Altura = Altura
        self.direcao = Operacoes.NormalizaVetor(direcao)
        self.material = material
        self.m = m
        self.tipo = tipo
        return

    def Calcular_Normal(self,ponto):
        w = Operacoes.Subtracao_vetores(ponto,self.CentroBase)
        aux1 = Operacoes.ProdutoEscalar(w,self.direcao)
        aux2 = Operacoes.Vetor_escalar(self.direcao,aux1)
        PP = Operacoes.Soma_vetores(self.CentroBase,aux2)
        return PP

    def IntercecaoRaioCilindro(self, raio1):
        D = raio1.Direcao
        posicaoOlhoObservador = raio1.Origem
        prod_escalar = Operacoes.ProdutoEscalar(D, self.direcao)
    
        mult = Operacoes.Vetor_escalar(self.direcao, prod_escalar )
    
        w = Operacoes.Subtracao_vetores(D, mult)

 
        v_primeiro = Operacoes.Subtracao_vetores(posicaoOlhoObservador, self.CentroBase )
        v_segundo = Operacoes.Vetor_escalar(self.direcao,Operacoes.ProdutoEscalar(v_primeiro, self.direcao) ) 
        v = Operacoes.Subtracao_vetores(v_primeiro, v_segundo)
    
        a = Operacoes.ProdutoEscalar(w, w)
        b = 2*Operacoes.ProdutoEscalar(v, w)
        c = Operacoes.ProdutoEscalar(v, v) - (self.RaioBase * self.RaioBase)
    
        delta = (pow(b,2) - (4* a * c))
  
        if(delta < 0):
            return math.inf
    
        t1 = (-b + math.sqrt(delta)) / (2*a)
        t2 = (-b - math.sqrt(delta)) / (2*a)
    
        if(t1 < t2):
            t2 = t1

        pt1 = Operacoes.EquacaoReta(t2,raio1)
        w = Operacoes.Subtracao_vetores(pt1,self.CentroBase)
        aux3 = Operacoes.ProdutoEscalar(w,self.direcao)
        
        if aux3 > self.Altura or aux3 < 0:
            return math.inf
        return  pt1
    
    