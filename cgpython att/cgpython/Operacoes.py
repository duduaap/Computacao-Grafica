import math
import numpy as np
from Vetor import Vetor
from Intercecoes import intercecao
from Raio import Raio
def Ponto(x, y, z):
    return {'x': x, 'y': y, 'z': z}

def ProdutoVetorial(vetor_A, vetor_B):
    x = vetor_A.y *vetor_B.z - vetor_A.z*vetor_B.y
    y = vetor_A.z*vetor_B.x - vetor_A.x*vetor_B.z
    z = vetor_A.x *vetor_B.y - vetor_A.y*vetor_B.x
    r = Vetor(x,y,z)
    return r

def ProdutoEscalar(v_1, v):
    return ((getattr(v_1, 'x')) * (getattr(v, 'x')) + (getattr(v_1, 'y')) * (getattr(v, 'y')) + (getattr(v_1, 'z')) * (getattr(v, 'z')))

def DistanciaEntrePontos(vetor1, vetor2):    
    return np.sqrt(np.square(getattr(vetor1,'x') - getattr(vetor2,'x'))+np.square(getattr(vetor1,'y') - getattr(vetor2,'y'))+np.square(getattr(vetor1,'z') - getattr(vetor2,'z')))

def EquacaoReta(vetort, raio):
    return Vetor(getattr(getattr(raio, "Origem"), "x") + vetort*getattr(getattr(raio, "Direcao"), "x"),getattr(getattr(raio, "Origem"), "y") + vetort*getattr(getattr(raio, "Direcao"), "y"), getattr(getattr(raio, "Origem"), "z") + vetort*getattr(getattr(raio, "Direcao"), "z"))

def NormalizaVetor(vetor):
    aux = math.sqrt(ProdutoEscalar(vetor,vetor))
    return Vetor((getattr(vetor, 'x'))/aux , (getattr(vetor, 'y'))/aux, (getattr(vetor, 'z'))/aux)

def Vetor_escalar(vetor, escalar):
    return Vetor(getattr(vetor,"x")*escalar, getattr(vetor,"y")*escalar, getattr(vetor,"z")*escalar)

def Subtracao_vetores(v_1, v):
    return Vetor((getattr(v_1, 'x')) - (getattr(v, 'x')), (getattr(v_1, 'y')) - (getattr(v, 'y')), (getattr(v_1, 'z')) - (getattr(v, 'z')))

def Soma_vetores(v_1, v):
    return Vetor((getattr(v_1, 'x')) + (getattr(v, 'x')), (getattr(v_1, 'y')) + (getattr(v, 'y')), (getattr(v_1, 'z')) + (getattr(v, 'z')))

def Operacao_Arroba(v_1, v):
    return Vetor((getattr(v_1, 'x')) * (getattr(v, 'x')), (getattr(v_1, 'y')) * (getattr(v, 'y')), (getattr(v_1, 'z')) * (getattr(v, 'z')))



def DecideCor(list_obj,objeto, Raio1, list_luz, t):
        
        Ld = Vetor(0,0,0)
        Le = Vetor(0,0,0)
        vetor_direcao = getattr(Raio1,"Direcao")
        n = objeto.Calcular_Normal(t)
        for luz in list_luz:
            if luz.tipo == "direcional":
                l = Vetor_escalar(luz.direcao,-1)
                int_luz = Raio(t,l)
            else:
                l = NormalizaVetor(Subtracao_vetores(getattr(luz,"posicao"),t))
                int_luz = Raio(t, NormalizaVetor(Subtracao_vetores(luz.posicao,t)))
            cor = True
            for obj in list_obj:
                aux2 = intercecao(obj,int_luz)
                if aux2 != math.inf:
                    if luz.tipo == "direcional":
                        if DistanciaEntrePontos(aux2, t) > 0.0001:
                            cor = False
                    else:
                        if DistanciaEntrePontos(aux2, t) < DistanciaEntrePontos(t,luz.posicao) and DistanciaEntrePontos(aux2, t) > 0.0001:
                            cor = False
            luz_dentro = True
            if luz.tipo == "spot":
                cosalfa = -(ProdutoEscalar(l,luz.direcao))
                if cosalfa < math.cos(luz.abertura):
                    luz_dentro = False
            if cor != False and luz_dentro == True:
                Ld = Soma_vetores(Ld,Vetor_escalar(Operacao_Arroba((getattr(luz, "intensidade")),objeto.material),max(ProdutoEscalar(l,n),0)))
                v = Vetor(- getattr(vetor_direcao,"x"), - getattr(vetor_direcao,"y"),- getattr(vetor_direcao,"z"))
                aux = Vetor_escalar(n,2*ProdutoEscalar(n,l))
                r = Vetor(getattr(aux,"x") - getattr(l,"x"),getattr(aux,"y") - getattr(l,"y"),getattr(aux,"z") - getattr(l,"z"))
                Le =  Soma_vetores(Le,Vetor_escalar(Operacao_Arroba((getattr(luz, "intensidade")),objeto.material), (max(ProdutoEscalar(r,v),0))**objeto.m))
                if luz.tipo == "spot":
                    Le = Vetor_escalar(Le, cosalfa)
                
        La = Operacao_Arroba(Vetor(0.3,0.3,0.3),objeto.material)
        L = Soma_vetores(Soma_vetores(La,Le),Ld)
        aux = max(L.x,L.y,L.z)
        if aux > 1:
                L.x = L.x/aux
                L.y = L.y/aux
                L.z = L.z/aux
                

        return Vetor_escalar(L,255)