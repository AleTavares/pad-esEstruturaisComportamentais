from .implementacao import Pedido, FreteNormal, FreteExpresso, FreteRetiradaLocal

def main():
    """Função principal para demonstrar o uso do padrão Strategy."""
    print("--- Padrão Strategy ---")

    # Um pedido de 2kg
    peso_pedido = 2.0

    # Cliente escolhe o frete normal
    frete_normal = FreteNormal()
    pedido = Pedido(peso_pedido, frete_normal)
    pedido.calcular_custo_total()

    # Cliente decide mudar para frete expresso
    frete_expresso = FreteExpresso()
    pedido.definir_estrategia_frete(frete_expresso)
    pedido.calcular_custo_total()

    # Outro cliente opta pela retirada local
    frete_retirada = FreteRetiradaLocal()
    pedido.definir_estrategia_frete(frete_retirada)
    pedido.calcular_custo_total()

    print("---------------------\n")
