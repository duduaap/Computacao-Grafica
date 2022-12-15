import Operacoes
import math
class Malha:
    def __init__(self,listaFaces,material,m,tipo):
        self.listaFaces = listaFaces
        self.material = material
        self.m = m
        self.tipo = tipo
        return
    
    def checar_ponto_face(self,ponto,face):
        c1 = Operacoes.ProdutoEscalar(Operacoes.ProdutoVetorial(Operacoes.Subtracao_vetores(face.ponto3,ponto),Operacoes.Subtracao_vetores(face.ponto1,ponto)),face.Calcular_Normal())/Operacoes.ProdutoEscalar(Operacoes.ProdutoVetorial(Operacoes.Subtracao_vetores(face.ponto1,face.ponto2),Operacoes.Subtracao_vetores(face.ponto1,face.ponto3)),face.Calcular_Normal())
        c2 = Operacoes.ProdutoEscalar(Operacoes.ProdutoVetorial(Operacoes.Subtracao_vetores(face.ponto1,ponto),Operacoes.Subtracao_vetores(face.ponto2,ponto)),face.Calcular_Normal())/Operacoes.ProdutoEscalar(Operacoes.ProdutoVetorial(Operacoes.Subtracao_vetores(face.ponto2,face.ponto3),Operacoes.Subtracao_vetores(face.ponto2,face.ponto1)),face.Calcular_Normal())
        c3 = Operacoes.ProdutoEscalar(Operacoes.ProdutoVetorial(Operacoes.Subtracao_vetores(face.ponto2,ponto),Operacoes.Subtracao_vetores(face.ponto3,ponto)),face.Calcular_Normal())/Operacoes.ProdutoEscalar(Operacoes.ProdutoVetorial(Operacoes.Subtracao_vetores(face.ponto3,face.ponto1),Operacoes.Subtracao_vetores(face.ponto3,face.ponto2)),face.Calcular_Normal())
        if c1 < 0 or c2 < 0 or c3 < 0:
            return False
        else:
            return True
        
        
    def Calcular_Normal(self,ponto):
        for i in self.listaFaces:
            if self.checar_ponto_face(ponto,i) == True:
                norm = i.Calcular_Normal()
                
                return Operacoes.NormalizaVetor(norm)

    def IntersecaoRaioMalha(self,raio):
        distanciaobsv = 100000
        ponto_intersecao = math.inf
        for i in self.listaFaces:
            inte = i.plano.IntercecaoPlano(raio)
            if inte != math.inf:
                if self.checar_ponto_face(inte,i) == True:
                    if Operacoes.DistanciaEntrePontos(inte, raio.Origem) < distanciaobsv:
                        distanciaobsv = Operacoes.DistanciaEntrePontos(inte, raio.Origem)
                        ponto_intersecao = inte
        return ponto_intersecao
    
    def mundoParaCamera(self, matriz):
        for face in self.listaFaces:
            face.mundoParaCamera(matriz)

        