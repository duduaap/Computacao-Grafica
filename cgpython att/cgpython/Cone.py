import Operacoes
import math
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
        return


    def Calcular_Normal(self,ponto):
        w2 = Operacoes.Subtracao_vetores(self.v,ponto)
        Nt = Operacoes.ProdutoVetorial(w2,self.direcao)
        N = Operacoes.ProdutoVetorial(w2,Nt)
        normal = Operacoes.NormalizaVetor(N)
        return normal

    def IntercecaoRaioCone(self, raio):
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

        if(a==0):
            if(b==0):
                return math.inf
        if(delta < 0):
            return math.inf
        
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
            
        w2 = Operacoes.Subtracao_vetores(pt1,self.v)
        aux3 = Operacoes.ProdutoEscalar(w2,self.direcao)
        
        if aux3 > self.Altura or aux3 < 0:
            
            return math.inf   
        
        return pt1