from asyncio.windows_events import NULL
import Operacoes
import numpy as np
import math

class Esfera:
    def __init__(self, rEsfera, CenterEsf, material, m, tipo):
        self.rEsfera = rEsfera
        self.CenterEsf = CenterEsf
        self.material = material
        self.m = m
        self.tipo = tipo
        return
        
    def intersecaoRaioEsfera(self,Raio1):
        posicaoOlhoObservador = getattr(Raio1, 'Origem')
        Dir = getattr(Raio1, 'Direcao')
        w = Operacoes.Subtracao_vetores(posicaoOlhoObservador,self.CenterEsf)
        a = Operacoes.ProdutoEscalar(Dir, Dir)
        b = 2*Operacoes.ProdutoEscalar(w, Dir)
        c = Operacoes.ProdutoEscalar(w, w) - pow(self.rEsfera,2) 
        
        

        delta = (pow(b,2) - (4* a * c))
        
        if(delta > 0):
            t1 = ((-b) + np.sqrt(delta)) / ( 2*a)
            t2 = ((-b) - np.sqrt(delta)) / ( 2*a)
        
            pt1 = Operacoes.EquacaoReta(t1, Raio1)
            pt2 = Operacoes.EquacaoReta(t2, Raio1)
            
            if(Operacoes.DistanciaEntrePontos(pt1,posicaoOlhoObservador) > Operacoes.DistanciaEntrePontos(pt2,posicaoOlhoObservador)):
                pt1 = pt2
                
                
        elif(delta == 0):
            t1 = ((-b) + np.sqrt(delta)) / ( a)
            pt1 = Operacoes.EquacaoReta(t1,Raio1)
        else:
            pt1 = math.inf
        result = pt1
        return result

    def Calcular_Normal(self,ponto):
        return Operacoes.NormalizaVetor(Operacoes.Subtracao_vetores(ponto,getattr(self,"CenterEsf")))
    
    def mundoParaCamera(self, matriz):
        
        self.CenterEsf = Operacoes.mult_matriz_ponto(matriz, self.CenterEsf)
    
    
    