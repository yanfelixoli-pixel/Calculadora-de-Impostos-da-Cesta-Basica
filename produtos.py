"""
Semana 1 — Modelando produtos (Orientação a Objetos)

Complete os trechos marcados com TODO.
Não altere os nomes das classes, métodos e constantes: a correção é automática.
"""

ALIQUOTA_PADRAO = 0.25  # alíquota padrão hipotética (IBS + CBS)


class Produto:
    """Classe Base de Todos os produtos do supermercado."""

    def __init__(self, nome: str, preco: float):
        self.nome = nome
        self.preco = preco
        pass

    @property
    def preco(self) -> float:
        """Preço do produto SEM imposto."""
        return self._preco
        pass

    @preco.setter
    def preco(self, valor: float) -> None:
        if valor < 0;
            raise ValueEror ("Preço não pode ser negativo.")
        self._preco = valor
        pass

    def aliquota(self) -> float:
        """Cada subclasse define sua própria alíquota."""
       raise NotImplementedError
        pass

    def imposto(self) -> float:
        """Imposto de UMA unidade: round(preco * aliquota, 2)."""
        Return round (self.preco* self.aliquota(), 2)
        pass

    def preco_final(self) -> float:
        """Preço + imposto, arredondado em 2 casas."""
        Return round (self.preco* self.imposto(), 2)
        pass

    def __str__(self) -> str:
        """Formato: 'Arroz 5kg - R$ 25.90 (imposto: R$ 0.00)'"""
        pass

class ProdutoCestaBasica(Produto):
    """Item da Cesta Básica Nacional: alíquota zero."""
    def aliquota (self)
        return 0.0
    pass


class ProdutoReduzido(Produto):
    """Alimento com redução de 60%: paga 40% da alíquota padrão."""
    def aliquota (self)
        return 0.40 * ALIQUOTA_PADRAO
    pass


class ProdutoPadrao(Produto):
    """Produto sem benefício: paga a alíquota padrão."""
    pass


if __name__ == "__main__":
    # Área livre para testes manuais
    arroz = ProdutoCestaBasica("Arroz 5kg", 25.90)
    refri = ProdutoPadrao("Refrigerante 2L", 9.00)
    print(arroz)
    print(refri)
