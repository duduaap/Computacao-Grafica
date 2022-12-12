from Esfera import Esfera
from Vetor import Vetor
from Plano import Plano
from Cilindro import Cilindro
from Cone import Cone
from Luz_Pontual import Luz_Pontual
from Luz_Spot import Luz_Spot
from Luz_Direcional import Luz_Direcional
from Ponto import Ponto
from Aresta import Aresta
from Face import Face
from Malha import Malha
from math import sqrt
from Operacoes import NormalizaVetor
from Operacoes import Subtracao_vetores
def listar_objetos():

    ##esfera1 = Esfera(40, Vetor(0, 0, -100), Vetor(0.7, 0.2, 0.2),10,"esfera")
    
    planoChao = Plano(Vetor(0,-40,0),Vetor(0,1,0), Vetor(0.2, 0.7, 0.2),1,"plano")
    
    planoParede = Plano(Vetor(0,0,-200),Vetor(0,0,1), Vetor(0.3, 0.3, 0.7),1,"plano")
    
    ##cilindro1 = Cilindro(Vetor(0,0,-100), 13, 120, Vetor(-1/sqrt(3), -1/sqrt(3), 1/sqrt(3)),Vetor( 0.8, 0.3, 0.2),10,"cilindro")
    
    ##cone1 = Cone(Vetor(0, 60, -100),60,20,Vetor(-1/sqrt(3), 1/sqrt(3), -1/sqrt(3)),Vetor( 0.8, 0.3, 0.2),10,"cone")
    
    ponto1 = Ponto(-50,0,-100)
    ponto2 = Ponto(50,0,-100)
    ponto5 = Ponto(-50,50,-100)
    ponto6 = Ponto(50,50,-100)
    ponto3 = Ponto(-50,0,-50)
    ponto4 = Ponto(50,0,-50)
    ponto7 = Ponto(-50,50,-50)
    ponto8 = Ponto(50,50,-50)
    
    face1= Face(ponto1,ponto2,ponto6)
    face2=Face(ponto6,ponto5,ponto1)
    face3=Face(ponto2,ponto4,ponto8)
    face4=Face(ponto8,ponto6,ponto2)
    face5=Face(ponto4,ponto3,ponto7)
    face6=Face(ponto7,ponto8,ponto4)
    face7=Face(ponto3,ponto1,ponto5)
    face8=Face(ponto5,ponto7,ponto3)
    face9=Face(ponto5,ponto6,ponto8)
    face10=Face(ponto8,ponto7,ponto5)
    face11=Face(ponto3,ponto4,ponto2)
    face12=Face(ponto2,ponto1,ponto3)
    
    lista_face = []
    lista_face.append(face1)
    lista_face.append(face2)
    lista_face.append(face3)
    lista_face.append(face4)
    lista_face.append(face5)
    lista_face.append(face6)
    lista_face.append(face7)
    lista_face.append(face8)
    lista_face.append(face9)
    lista_face.append(face10)
    lista_face.append(face11)
    lista_face.append(face12)
    
    cubo1 = Malha(lista_face,Vetor(1, 0.078, 0.576),10,"malha")
    
    lista_obj = []
    ##lista_obj.append(esfera1)
    lista_obj.append(planoParede)
    lista_obj.append(planoChao)
    lista_obj.append(cubo1)
    ##lista_obj.append(cilindro1)
    ##lista_obj.append(cone1)

    return lista_obj


def listar_luzes():
    
    luz_pontual = Luz_Pontual(Vetor(0,60,30),Vetor(0.7,0.7,0.7),"pontual")
    ##luz_spot = Luz_Spot(Vetor(0,60,30),Vetor(0.7,0.7,0.7),NormalizaVetor(Subtracao_vetores(Vetor(0, 30, -100),Vetor(0,60,30))),0.5,"spot")
    ##luz_direcional = Luz_Direcional(Vetor(-1,-1,-1),Vetor(0.7,0.7,0.7),"direcional")
    lista_luzes = []
    lista_luzes.append(luz_pontual)
    ##lista_luzes.append(luz_spot)
    ##lista_luzes.append(luz_direcional)
    
    return lista_luzes