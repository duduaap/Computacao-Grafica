from asyncio.windows_events import NULL
import Operacoes
import numpy as np
import math
from Plano import Plano
from Vetor import Vetor
class Cilindro:
    def __init__(self,CentroBase,RaioBase,Altura,direcao,material, m,tipo):
        self.CentroBase = CentroBase
        self.RaioBase = RaioBase
        self.Altura = Altura
        self.direcao = Operacoes.NormalizaVetor(direcao)
        self.material = material
        self.m = m
        self.tipo = tipo
        self.local_intersecao = 0
        self.plano_base = Plano(self.CentroBase,Operacoes.Vetor_escalar(self.direcao,-1),self.material,1,"plano")
        self.plano_topo = Plano(Operacoes.Soma_vetores(self.CentroBase,Operacoes.Vetor_escalar(self.direcao,self.Altura)),self.direcao,self.material,1,"plano")
        return

    def Calcular_Normal(self,ponto):
        
        if self.local_intersecao == "base":
            return Operacoes.Vetor_escalar(self.direcao,-1)
        
        if self.local_intersecao == "topo":
            return self.direcao
        
        if self.local_intersecao == "corpo":
            w = Operacoes.Subtracao_vetores(ponto,self.CentroBase)
            aux1 = Operacoes.ProdutoVetorial(w,self.direcao)
            aux2 = Operacoes.ProdutoVetorial(self.direcao,aux1)
            return Operacoes.NormalizaVetor(aux2)

    def reCalculaPlanos(self):
        nova_basePlano_plano = Plano(self.CentroBase, Operacoes.Vetor_escalar(self.direcao,-1), self.material,self.m,"plano")
        self.plano_base = nova_basePlano_plano
        centroTopo = Operacoes.Soma_vetores(self.CentroBase, Operacoes.Vetor_escalar(
        self.direcao, self.Altura))
        novo_topoPlano = Plano(centroTopo, self.direcao, self.material,self.m,"plano")
        self.plano_topo = novo_topoPlano
    
    
    def mundoParaCamera(self, matriz):
        self.CentroBase = Operacoes.mult_matriz_ponto(matriz, self.CentroBase)
        self.direcao = Operacoes.NormalizaVetor(Operacoes.mult_matriz_vetor(matriz, self.direcao))
        self.reCalculaPlanos()


    def IntercecaoRaioCilindro(self, raio1):
        
        aux1 = self.plano_base.IntercecaoPlano(raio1)
        aux2 = self.plano_topo.IntercecaoPlano(raio1)
        
        
        if aux1 == math.inf or Operacoes.DistanciaEntrePontos(aux1,self.CentroBase) > self.RaioBase:
            aux1 = math.inf
        if aux2 == math.inf or Operacoes.DistanciaEntrePontos(aux2,Operacoes.Soma_vetores(self.CentroBase,Operacoes.Vetor_escalar(self.direcao,self.Altura))) > self.RaioBase:
            aux2 = math.inf
        
        D = raio1.Direcao
        origem = raio1.Origem
        
        prod_escalar = Operacoes.ProdutoEscalar(D, self.direcao)
        mult = Operacoes.Vetor_escalar(self.direcao, prod_escalar)
    
        w = Operacoes.Subtracao_vetores(D, mult)

 
        v1 = Operacoes.Subtracao_vetores(origem, self.CentroBase)
        v2 = Operacoes.Vetor_escalar(self.direcao,Operacoes.ProdutoEscalar(v1, self.direcao)) 
        v = Operacoes.Subtracao_vetores(v1,v2)
    
        a = Operacoes.ProdutoEscalar(w, w)
        b = 2*Operacoes.ProdutoEscalar(v, w)
        c = Operacoes.ProdutoEscalar(v, v) - (self.RaioBase * self.RaioBase)
    
        delta = (pow(b,2) - (4* a * c))
  
        if(delta < 0):
            pt1 = math.inf
        else:
            t1 = (-b + math.sqrt(delta)) / (2*a)
            t2 = (-b - math.sqrt(delta)) / (2*a)
    
            if(t1 < t2):
                t2 = t1

            pt1 = Operacoes.EquacaoReta(t2,raio1)

            w = Operacoes.Subtracao_vetores(pt1,self.CentroBase)
            aux3 = Operacoes.ProdutoEscalar(w,self.direcao)
        
            if aux3 > self.Altura or aux3 < 0:
                pt1 = math.inf
        
        
        if aux1 == math.inf:
            dist_aux1 = math.inf
        else:
            dist_aux1 = Operacoes.DistanciaEntrePontos(aux1,origem)
            
            
        if aux2 == math.inf:
            dist_aux2 = math.inf 
        else:
            dist_aux2 = Operacoes.DistanciaEntrePontos(aux2,origem)
            
            
        if pt1 == math.inf:
            dist_pt1 = math.inf
        else:
            dist_pt1 = Operacoes.DistanciaEntrePontos(pt1,origem)
        
        
        self.local_intersecao = "corpo"
        
        if dist_aux1 < dist_aux2 and dist_aux1 < dist_pt1:
            pt1 = aux1
            self.local_intersecao = "base"
            
        if dist_aux2 < dist_aux1 and dist_aux2 < dist_pt1:
            pt1 = aux2
            self.local_intersecao = "topo"

        return  pt1
