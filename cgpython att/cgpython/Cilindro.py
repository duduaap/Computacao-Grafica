from asyncio.windows_events import NULL
import Operacoes
import numpy as np
import math

class Cilindro:
    def __init__(self,CentroBase,RaioBase,Altura,direcao,material, m,tipo):
        self.CentroBase = CentroBase
        self.RaioBase = RaioBase
        self.Altura = Altura
        self.direcao = direcao
        self.material = material
        self.m = m
        self.tipo = tipo
        return
    
    def IntercecaoRaioCilindro(self, raio1):
        
        return