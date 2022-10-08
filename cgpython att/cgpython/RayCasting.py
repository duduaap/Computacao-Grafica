from Janela import Janela
from Esfera import Esfera
from Raio import Raio
from Vetor import Vetor
from PIL import Image


def rayCasting():
   nCol = 100
   nLin = 100
   janela = Janela(100, 100, 10)
   esfera1 = Esfera(35, Vetor(0, 0, getattr(janela, 'dJanela') + 40), Vetor(255,0,0))
   observer = Vetor(0,0,0)
   Dx = janela.wJanela/nCol
   Dy = janela.hJanela/nLin
   
   image = Image.new(mode="RGB", size=(100, 100))
   pixels = image.load()
   for l in range (nLin):
      for c in range (nCol):
          
          x = -(janela.wJanela/2) + (Dx/2) + (Dx*c)
          y = (janela.hJanela/2) - (Dy/2) - (Dy*l)
          PontoTela = Vetor(x, y, janela.dJanela)
          Raio2 = Raio(observer, PontoTela)
          color = Esfera.DecideCor(esfera1, Raio2)
          
          pixels[l, c] = (color.x, color.y, color.z)
   print (pixels)
   image.save("esfera.png", format="png")
   image.show()
   
   
rayCasting()


           
           





