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
import Transformacoes

def listar_objetos():

    esfera1 = Esfera(1, Vetor(0,-38,40), Vetor(0.7, 0.2, 0.2),10,"esfera")
    
    planoChao = Plano(Vetor(0, -40, 0),Vetor(0,1,0), Vetor(0.2, 0.7, 0.2),1,"plano")
    
    planoParede = Plano(Vetor(0, 0, 200),Vetor(0,0,1), Vetor(0.3, 0.3, 0.7),1,"plano")
    
    #cilindro1 = Cilindro(Vetor(0,0,-100), 13, 120, Vetor(1,1,0),Vetor( 0.8, 0.3, 0.2),10,"cilindro")
    
    #cone1 = Cone(Vetor(0, 0, -100),60,20,Vetor(1, 1, 0),Vetor( 0.8, 0.3, 0.2),10,"cone")
    
    
    

    #PARALELEPIPEDOS ARQUIBANCADA
    p1 = Ponto(39,-40,80) 
    p2 = Ponto(40,-40,100) 
    p3 = Ponto(40,-38,100) 
    p4 = Ponto(39,-40,80) 
    p5 = Ponto(40,-36,100) 
    p6 = Ponto(39,-36,90) 
    p7 = Ponto(39,-38,80) 
    p8 = Ponto(-40,-40,80) 
    p9 = Ponto(-40,-40,100) 
    p10 = Ponto(-40,-38,100) 
    p11 = Ponto(-39,-40,80) 
    p12 = Ponto(-40,-36,100) 
    p13 = Ponto(-39,-36,90) 
    p14 = Ponto(-39,-38,80) 

    
    
    cilindro_meio_campo = Cilindro(Vetor(0,-40,40),11,0.1,Vetor(0,1,0),Vetor(1,1,1),10,"cilindro")
    cilindro_meio_campo2 = Cilindro(Vetor(0,-40,40),9,0.15,Vetor(0,1,0),Vetor(0.2, 0.7, 0.2),10,"cilindro")
    cilindro_trave_esquerda1 = Cilindro(Vetor(30,-40,30),0.5,10,Vetor(0,1,0),Vetor(1,1,1),10,"cilindro")
    cilindro_trave_esquerda2 = Cilindro(Vetor(40,-40,50),0.5,10,Vetor(0,1,0),Vetor(1,1,1),10,"cilindro")
    cilindro_trave_esquerda3 = Cilindro(Vetor(30,-30,30),0.5,20,Vetor(0.5,0,1),Vetor(1,1,1),10,"cilindro")
    cilindro_trave_direita1 = Cilindro(Vetor(-30,-40,30),0.5,10,Vetor(0,1,0),Vetor(1,1,1),10,"cilindro")
    cilindro_trave_direita2 = Cilindro(Vetor(-40,-40,50),0.5,10,Vetor(0,1,0),Vetor(1,1,1),10,"cilindro")
    cilindro_trave_direita3 = Cilindro(Vetor(-30,-30,30),0.5,20,Vetor(-0.5,0,1),Vetor(1,1,1),10,"cilindro")

    MarcaCampoEF = Cilindro(Vetor(27,-40,25),0.3,45,Vetor(0.5,0,1),Vetor(1,1,1),10,"cilindro")
    MarcaCampoDF = Cilindro(Vetor(-27,-40,25),0.3,45,Vetor(-0.5,0,1),Vetor(1,1,1),10,"cilindro")
    MarcaCampoLL = Cilindro(Vetor(50,-40,68 ),0.3, 100, Vetor(-1,0,0),Vetor(1,1,1),10,"cilindro")
    MarcaCampoLP = Cilindro(Vetor(27,-40,25),0.3, 54, Vetor(-1,0,0),Vetor(1,1,1),10,"cilindro")
    MarcaCampoM = Cilindro(Vetor(0,-40,25),0.3,47,Vetor(0,0,1),Vetor(1,1,1),10,"cilindro")
    
    poste1 = Cilindro(Vetor(40,-40,80),1,30,Vetor(0,1,0),Vetor(0.5,0.5,0.5),10,"cilindro")
    poste2 = Cilindro(Vetor(40,-10,80),0.7,7,Vetor(0.9,0,1),Vetor(0.5,0.5,0.5),10,"cilindro")
    cone_poste = Cone(Vetor(40,-10,75),1.7,5,Vetor(0,1,0),Vetor(0.5,0.5,0.5),10,"cone")
    


    #paralelogramo generico
    ponto1 = Ponto(-30,0,-100)
    ponto2 = Ponto(30,0,-100)
    ponto3 = Ponto(-20,0,-95)
    ponto4 = Ponto(20,0,-95)
    ponto5 = Ponto(-30,5,-100)
    ponto6 = Ponto(30,5,-100)
    ponto7 = Ponto(-20,5,-95)
    ponto8 = Ponto(20,5,-95)
    face1 = Face(ponto1,ponto2,ponto6)
    face2 = Face(ponto6,ponto5,ponto1)
    face3 = Face(ponto2,ponto4,ponto8)
    face4 = Face(ponto8,ponto6,ponto2)
    face5 = Face(ponto4,ponto3,ponto7)
    face6 = Face(ponto7,ponto8,ponto4)
    face7 = Face(ponto3,ponto1,ponto5)
    face8 = Face(ponto5,ponto7,ponto3)
    face9 = Face(ponto5,ponto6,ponto8)
    face10 = Face(ponto8,ponto7,ponto5)
    face11 = Face(ponto3,ponto4,ponto2)
    face12 = Face(ponto2,ponto1,ponto3)
    
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
    
    #cubo1 = Malha(lista_face,Vetor(0.1, 0.1, 0.1),10,"malha")


    lista_obj = []
    lista_obj.append(esfera1)
    lista_obj.append(planoParede)
    lista_obj.append(planoChao)
    lista_obj.append(cilindro_meio_campo)
    lista_obj.append(cilindro_meio_campo2)
    lista_obj.append(cilindro_trave_esquerda1)
    lista_obj.append(cilindro_trave_esquerda2)
    lista_obj.append(cilindro_trave_esquerda3)
    lista_obj.append(cilindro_trave_direita1)
    lista_obj.append(cilindro_trave_direita2)
    lista_obj.append(cilindro_trave_direita3) 
    lista_obj.append(MarcaCampoDF)
    lista_obj.append(MarcaCampoEF)
    lista_obj.append(MarcaCampoLL)
    lista_obj.append(MarcaCampoLP)
    lista_obj.append(MarcaCampoM)
    lista_obj.append(poste1)
    lista_obj.append(poste2)
    #lista_obj.append(cubo1)
    lista_obj.append(cone_poste)

    return lista_obj


def listar_luzes():
    
    luz_pontual = Luz_Pontual(Vetor(0, 60, -30),Vetor(0.7,0.7,0.7),"pontual")
    luz_spot = Luz_Spot(Vetor(0,60,30),Vetor(0.7,0.7,0.7),Vetor(0,-40,40),0.5,"spot")
    luz_direcional = Luz_Direcional(Vetor(-1,-1,-1),Vetor(0.7,0.7,0.7),"direcional")
    lista_luzes = []
    lista_luzes.append(luz_pontual)
    #lista_luzes.append(luz_spot)
    ##lista_luzes.append(luz_direcional)
    
    return lista_luzes