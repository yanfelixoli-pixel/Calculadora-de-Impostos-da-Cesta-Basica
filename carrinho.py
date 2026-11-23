"""
Semana 2 — O carrinho de compras (Orientação a Objetos: composição)

Complete os trechos marcados com TODO.
Não altere os nomes da classe e dos métodos: a correção é automática.
"""

from produtos import ALIQUOTA_PADRAO, Produto


class Carrinho:
    """Guarda produtos e suas quantidades."""

    def __init__(self):
        # Sugestão: um dicionário  nome -> [produto, quantidade]
        self._itens = {}

    def adicionar(self, produto: Produto, quantidade: int = 1) -> None:
        if not isinstance(produto, Produto):
            raise TypeError("produto deve ser uma instância de Produto")
        if not isinstance(quantidade, int) or quantidade < 1:
            raise ValueError("quantidade deve ser um inteiro >= 1")

        if produto.nome in self._itens:
            self._itens[produto.nome][1] += quantidade
        else:
            self._itens[produto.nome] = [produto, quantidade]
        pass

    def remover(self, nome: str) -> None:
        if nome not in self._itens:
            raise KeyError(nome)
        del self._itens[nome]
        pass

    def subtotal(self) -> float:
        return round(sum(produto.preco * qtd for produto, qtd in self._itens.values()), 2)
        pass

    def total_impostos(self) -> float:
        return round(sum(produto.imposto() * qtd for produto, qtd in self._itens.values()), 2)
        pass

    def total(self) -> float:
        return round(self.subtotal() + self.total_impostos(), 2)
        pass

    def economia(self) -> float:
        total_se_fosse_padrao = sum(
            round(produto.preco * ALIQUOTA_PADRAO, 2) * qtd
            for produto, qtd in self._itens.values()
        )
        return round(total_se_fosse_padrao - self.total_impostos(), 2)
        pass

    def __len__(self) -> int:
        return sum(qtd for _, qtd in self._itens.values())
        pass

    def __contains__(self, nome: str) -> bool:
        return nome in self._itens
        pass


if __name__ == "__main__":
    from produtos import ProdutoCestaBasica, ProdutoPadrao

    c = Carrinho()
    c.adicionar(ProdutoCestaBasica("Feijão 1kg", 8.00), 2)
    c.adicionar(ProdutoPadrao("Chocolate", 10.00))
    print("Total:", c.total())
    print("Economia:", c.economia())
