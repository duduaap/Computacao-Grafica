from Esfera import Esfera
from Vetor import Vetor
from Plano import Plano
from Luz_Pontual import Luz_Pontual
def listar_objetos():

    esfera1 = Esfera(40, Vetor(0, 0, -100), Vetor(0.7, 0.2, 0.2),10,"esfera")
    
    planoChao = Plano(Vetor(0,-40,0),Vetor(0,1,0), Vetor(0.2, 0.7, 0.2),1,"plano")
    
    planoParede = Plano(Vetor(0,0,-200),Vetor(0,0,1), Vetor(0.3, 0.3, 0.7),1,"plano")
    
    lista_obj = []
    lista_obj.append(esfera1)
    lista_obj.append(planoParede)
    lista_obj.append(planoChao)

    return lista_obj


def listar_luzes():
    
    luz_pontual = Luz_Pontual(Vetor(0,60,30),Vetor(0.7,0.7,0.7))
    lista_luzes = []
    lista_luzes.append(luz_pontual)
    
    return lista_luzes