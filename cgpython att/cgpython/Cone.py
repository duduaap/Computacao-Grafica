import Operacoes
import math
from Plano import Plano
from Vetor import Vetor
class Cone:
    def __init__(self,CentroBase,RaioBase,Altura,direcao,material,m,tipo):
        h_dc = Operacoes.Vetor_escalar(direcao,Altura )
        self.v = Operacoes.Soma_vetores(CentroBase, h_dc)
        self.CentroBase = CentroBase
        self.RaioBase = RaioBase
        self.Altura = Altura
        self.direcao = Operacoes.NormalizaVetor(direcao)
        self.material = material
        self.m = m
        self.tipo = tipo
        self.local_intersecao = 0
        self.plano_base = Plano(self.CentroBase,Operacoes.Vetor_escalar(self.direcao,-1),self.material,self.m,"plano")
        return


    def Calcular_Normal(self,ponto):
        if self.local_intersecao == "base":
            return Operacoes.Vetor_escalar(self.direcao,-1)
        else:
            w2 = Operacoes.Subtracao_vetores(self.v,ponto)
            Nt = Operacoes.ProdutoVetorial(w2,self.direcao)
            N = Operacoes.ProdutoVetorial(w2,Nt)
            normal = Operacoes.NormalizaVetor(N)
            return normal
        
    def reCalculaPlanos(self):
        basePlano_cone = Plano(self.CentroBase, Operacoes.Vetor_escalar(self.direcao,-1), self.material,self.m,"plano")
        self.plano_base = basePlano_cone
    
    def mundoParaCamera(self, matriz):
        self.v = Operacoes.mult_matriz_ponto(matriz, self.v)
        self.CentroBase = Operacoes.mult_matriz_ponto(matriz, self.CentroBase)
        self.direcao = Operacoes.NormalizaVetor(Operacoes.mult_matriz_vetor(matriz, self.direcao))

        self.reCalculaPlanos()

    def IntercecaoRaioCone(self, raio):
        
        aux1 = self.plano_base.IntercecaoPlano(raio)
        
        if aux1 == math.inf or Operacoes.DistanciaEntrePontos(aux1,self.CentroBase) > self.RaioBase:
            aux1 = math.inf
        
        observer = raio.Origem
        D = raio.Direcao

        w = Operacoes.Subtracao_vetores(self.v, observer)

        cos2teta = (self.Altura*self.Altura)/(self.RaioBase*self.RaioBase + self.Altura*self.Altura)

        dr_dc = Operacoes.ProdutoEscalar(D, self.direcao)
        dr_dr = Operacoes.ProdutoEscalar(D,D)
        w_dc = Operacoes.ProdutoEscalar(w, self.direcao)
    
        a = (dr_dc * dr_dc) - (dr_dr*cos2teta)
        b_primeira_parte = Operacoes.ProdutoEscalar(w, D)* cos2teta
        b_segunda_parte = w_dc* dr_dc
        b = 2 * (b_primeira_parte - b_segunda_parte)
        c = w_dc * w_dc - Operacoes.ProdutoEscalar(w,w) * cos2teta

        delta = (pow(b,2) - (4* a * c))

        
        if(delta < 0) or (a == 0 and b ==0):
            pt1 = math.inf
        else:
            t1 = (-b + math.sqrt(delta)) / (2*a)
            t2 = (-b - math.sqrt(delta)) / (2*a)

            if(t1 > 0 and t2 > 0):
                if(t1 < t2):
                    t2 = t1
                pt1 = Operacoes.EquacaoReta(t2,raio)

            if(t1 < 0 and t2 > 0):
                pt1 = Operacoes.EquacaoReta(t2,raio)
            else:
                pt1 = Operacoes.EquacaoReta(t1,raio)
            
            w2 = Operacoes.Subtracao_vetores(pt1,self.CentroBase)
            aux3 = Operacoes.ProdutoEscalar(w2,self.direcao)
        
            if aux3 > self.Altura or aux3 < 0:
            
                pt1 = math.inf   

        if aux1 == math.inf:
            dist_aux1 = math.inf
        else:
            dist_aux1 = Operacoes.DistanciaEntrePontos(aux1,observer)
        if pt1 == math.inf:
            dist_pt1 = math.inf
        else:
            dist_pt1 = Operacoes.DistanciaEntrePontos(pt1,observer)
        
        self.local_intersecao = "corpo"
        if dist_aux1 < dist_pt1:
            pt1 = aux1
            self.local_intersecao = "base"   
        return pt1