import Operacoes
import math
class Cone:
    def __init__(self,CentroBase,RaioBase,Altura,direcao,material,m,tipo):
        h_dc = Operacoes.Vetor_escalar(direcao,Altura )
        v = Operacoes.Soma_vetores(CentroBase, h_dc)
        self.CentroBase = CentroBase
        self.RaioBase = RaioBase
        self.Altura = Altura
        self.direcao = direcao
        self.material = material
        self.m = m
        self.tipo = tipo
        return


    def Calcular_Normal():
        
        return

    def IntercecaoRaioCone(self, raio):
        observer = raio.Origem
        D = raio.Direcao

        w = Operacoes.Subtracao_vetores(self.v, observer)

        cos2teta = (self.Altura*self.Altura)/(self.RaioBase*self.RaioBase + self.Altura*self.Altura)

        dr_dc = Operacoes.Produto_escalar(D, self.direcao)
        dr_dr = Operacoes.Produto_escalar(D,D)
        w_dc = Operacoes.Produto_escalar(w, self.direcao)
    
        a = dr_dc * dr_dc - dr_dr*cos2teta
        b_primeira_parte = Operacoes.Produto_escalar(w, D)* cos2teta
        b_segunda_parte = w_dc* dr_dc
        b = 2 * (b_primeira_parte - b_segunda_parte)
        c = w_dc * w_dc - Operacoes.Produto_escalar(w,w) * cos2teta

        delta = b * b - 4* a * c

        if(a==0):
            if(b==0):
                return math.inf
            t1 = -c / 2*b
            pt1 = Operacoes.EquacaoReta(t1,raio)
            return pt1
    
        
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
            t1 = Operacoes.EquacaoReta(t1,raio)
        return pt1