

def intercecao(objeto,raio):
    if objeto.tipo == "esfera":
        pt1 = objeto.intersecaoRaioEsfera(raio)
    if objeto.tipo == "plano":
        pt1 = objeto.IntercecaoPlano(raio)
    if objeto.tipo == "cilindro":
        pt1 = objeto.IntercecaoRaioCilindro(raio)
    if objeto.tipo == "cone":
        pt1 = objeto.IntercecaoRaioCone(raio)
    if objeto.tipo == "malha":
        pt1 = objeto.IntersecaoRaioMalha(raio)
    return pt1