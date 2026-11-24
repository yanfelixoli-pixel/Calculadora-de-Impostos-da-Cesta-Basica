"""
Semana 3 — Reescrevendo com programação funcional
"""
from collections import namedtuple

ALIQUOTA_PADRAO = 0.25
ALIQUOTAS = {"cesta_basica": 0.0, "reduzido": 0.10, "padrao": 0.25}

Item = namedtuple("Item", ["nome", "preco", "categoria", "quantidade"], defaults=[1])

def aliquota(categoria):
    if categoria not in ALIQUOTAS:
        raise ValueError(f"Categoria inválida: {categoria}")
    return ALIQUOTAS[categoria]


  def imposto_item(item):
    imposto_unitario = round(item.preco * aliquota(item.categoria), 2)
    return round(imposto_unitario * item.quantidade, 2)


  def total_impostos(itens):
    return round(sum(map(imposto_item, itens)), 2)


  def total_compra(itens):
    subtotal = sum(item.preco * item.quantidade for item in itens)
    return round(subtotal + total_impostos(itens), 2)


  def filtrar_por_categoria(itens, categoria):
    return list(filter(lambda item: item.categoria == categoria, itens))


  def ordenar_por_preco(itens, decrescente=False):
    return sorted(itens, key=lambda item: item.preco, reverse=decrescente)


  def economia_total(itens):
    total_se_fosse_padrao = sum(
        round(round(item.preco * ALIQUOTA_PADRAO, 2) * item.quantidade, 2)
        for item in itens
    )
    return round(total_se_fosse_padrao - total_impostos(itens), 2)


  if __name__ == "__main__":
    itens = [
        Item("Arroz 5kg", 25.90, "cesta_basica", 2),
        Item("Chocolate", 10.00, "padrao"),
    ]
    print(total_impostos(itens))
    print(total_compra(itens))
    print(economia_total(itens))
