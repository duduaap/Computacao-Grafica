
from Operacoes import NormalizaVetor, Subtracao_vetores, ProdutoVetorial, ProdutoEscalar

class Camera: 

    def __init__(self, posicao, at, up):
        self.posicao = posicao
        self.at = at
        self.up = up
        self.mundoParaCamera = None

    def matriz(self):
        K = NormalizaVetor(Subtracao_vetores(self.at, self.posicao))
        viewUp = NormalizaVetor(Subtracao_vetores(self.up, self.posicao))
        I = NormalizaVetor(ProdutoVetorial(viewUp, K))
        J = NormalizaVetor(ProdutoVetorial(K, I))

        coluna4_I= - ProdutoEscalar(I, self.posicao)
        coluna4_J= - ProdutoEscalar(J, self.posicao)
        coluna4_K= - ProdutoEscalar(K, self.posicao)
    
        M = [[(getattr(I,'x')), (getattr(I,'y')), (getattr(I,'z')), coluna4_I], [(getattr(J,'x')), (getattr(J,'y')), (getattr(J,'z')), coluna4_J], [(getattr(K,'x')), (getattr(K,'y')), (getattr(K,'z')), coluna4_K], [0, 0, 0, 1]]

        return M