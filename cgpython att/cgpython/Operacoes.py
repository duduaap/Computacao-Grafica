from math import sqrt
import numpy as np
from Vetor import Vetor


def Ponto(x, y, z):
    return {'x': x, 'y': y, 'z': z}

def ProdutoVetorial(Vector, Vector2):
    return(np.cross(Vector, Vector2))

def ProdutoEscalar(v_1, v):
    return ((getattr(v_1, 'x')) * (getattr(v, 'x')) + (getattr(v_1, 'y')) * (getattr(v, 'y')) + (getattr(v_1, 'z')) * (getattr(v, 'z')))

def DistanciaEntrePontos(vetor1, vetor2):
    
    return np.sqrt(np.square(getattr(vetor1,'x') - getattr(vetor2,'x'))+np.square(getattr(vetor1,'y') - getattr(vetor2,'y'))+np.square(getattr(vetor1,'z') - getattr(vetor2,'z')))

def EquacaoReta(vetort, raio):
    return Vetor(getattr(getattr(raio, "Origem"), "x") + vetort*getattr(getattr(raio, "Direcao"), "x"),getattr(getattr(raio, "Origem"), "y") + vetort*getattr(getattr(raio, "Direcao"), "y"), getattr(getattr(raio, "Origem"), "z") + vetort*getattr(getattr(raio, "Direcao"), "z"))

def NormalizaVetor(vetor):
    aux = sqrt(ProdutoEscalar(vetor,vetor))
    return Vetor((getattr(vetor, 'x'))/aux , (getattr(vetor, 'y'))/aux, (getattr(vetor, 'z'))/aux)

def Vetor_escalar(vetor, escalar):
    return Vetor(vetor['x']*escalar, vetor['y']*escalar, vetor['z']*escalar)

def Subtracao_vetores(v_1, v):
    return Vetor((getattr(v_1, 'x')) - (getattr(v, 'x')), (getattr(v_1, 'y')) - (getattr(v, 'y')), (getattr(v_1, 'z')) - (getattr(v, 'z')))
