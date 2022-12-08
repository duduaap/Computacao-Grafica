from Esfera import Esfera
from Vetor import Vetor
from Plano import Plano
from Cilindro import Cilindro
from Cone import Cone
from Luz_Pontual import Luz_Pontual
from Luz_Spot import Luz_Spot
from Luz_Direcional import Luz_Direcional
from math import sqrt
from Operacoes import NormalizaVetor
from Operacoes import Subtracao_vetores
def listar_objetos():

    esfera1 = Esfera(40, Vetor(0, 0, -100), Vetor(0.7, 0.2, 0.2),10,"esfera")
    
    planoChao = Plano(Vetor(0,-40,0),Vetor(0,1,0), Vetor(0.2, 0.7, 0.2),1,"plano")
    
    planoParede = Plano(Vetor(0,0,-200),Vetor(0,0,1), Vetor(0.3, 0.3, 0.7),1,"plano")
    
    ##cilindro1 = Cilindro(Vetor(0,0,-100), 13, 120, Vetor(-1/sqrt(3), 1/sqrt(3), -1/sqrt(3)),Vetor( 0.8, 0.3, 0.2),10,"cilindro")
    
    ##cone1 = Cone(Vetor(0, 60, -100),60,20,Vetor(-1/sqrt(3), 1/sqrt(3), -1/sqrt(3)),Vetor( 0.8, 0.3, 0.2),10,"cone")
    
    lista_obj = []
    lista_obj.append(esfera1)
    lista_obj.append(planoParede)
    lista_obj.append(planoChao)
    ##lista_obj.append(cilindro1)
    ##lista_obj.append(cone1)

    return lista_obj


def listar_luzes():
    
    luz_pontual = Luz_Pontual(Vetor(0,60,30),Vetor(0.7,0.7,0.7),"pontual")
    luz_spot = Luz_Spot(Vetor(0,60,30),Vetor(0.7,0.7,0.7),NormalizaVetor(Subtracao_vetores(Vetor(0, 30, -100),Vetor(0,60,30))),0.5,"spot")
    luz_direcional = Luz_Direcional(Vetor(-1,-1,-1),Vetor(0.7,0.7,0.7),"direcional")
    lista_luzes = []
    lista_luzes.append(luz_pontual)
    lista_luzes.append(luz_spot)
    lista_luzes.append(luz_direcional)
    
    return lista_luzes