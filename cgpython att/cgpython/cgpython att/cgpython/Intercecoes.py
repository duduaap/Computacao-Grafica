

def intercecao(objeto,raio):
    if objeto.tipo == "esfera":
        pt1 = objeto.intersecaoRaioEsfera(raio)
    if objeto.tipo == "plano":
        pt1 = objeto.IntercecaoPlano(raio)
    
    return pt1