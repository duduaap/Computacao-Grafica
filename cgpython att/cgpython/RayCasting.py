from Janela import Janela
from Raio import Raio
from Vetor import Vetor
from PIL import Image
from Cenario import listar_objetos
from Cenario import listar_luzes
from Luz_Pontual import Luz_Pontual
import Operacoes
import math
from Intercecoes import intercecao
def rayCasting():
   nCol = 500
   nLin = 500
   janela = Janela(60, 60, -30)
   list_luzes = listar_luzes()

   observer = Vetor(0,0,0)
   Dx = janela.wJanela/nCol
   Dy = janela.hJanela/nLin
   list_obj = listar_objetos()
   image = Image.new(mode="RGB", size=(500, 500))
   pixels = image.load()
   obj_prox = 0
   for l in range (nLin):
      for c in range (nCol):
         x = -(janela.wJanela/2) + (Dx/2) + (Dx*c)
         y = (janela.hJanela/2) - (Dy/2) - (Dy*l)
         PontoTela = Operacoes.NormalizaVetor(Vetor(x, y, janela.dJanela))
         Raio2 = Raio(observer, PontoTela)
         objint = False
         distanciaorig = 10000
         for t in list_obj:
            p_int = intercecao(t,Raio2)
            if p_int != math.inf:
               if Operacoes.DistanciaEntrePontos(observer, p_int) < distanciaorig:
                  distanciaorig = Operacoes.DistanciaEntrePontos(observer, p_int)
                  obj_prox = t
                  p_intercecao = p_int
                  objint = True
         if objint == True:
            color = Operacoes.DecideCor(list_obj,obj_prox, Raio2, list_luzes,p_intercecao)
         else:
            color = Vetor(100,100,100)
            
         pixels[c, l] = (int(color.x), int(color.y), int(color.z))
   print (pixels)
   image.save("esfera.png", format="png")
   image.show()

rayCasting()


           
           





