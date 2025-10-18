from .implementacao import CafeSimples, Leite, Acucar

def main():
    """Função principal para demonstrar o uso do padrão Decorator."""
    print("--- Padrão Decorator ---")

    # Cria um café simples
    cafe = CafeSimples()
    print(f"Pedido: {cafe.get_descricao()} | Custo: R${cafe.get_custo():.2f}")

    # Adiciona leite ao café
    cafe_com_leite = Leite(cafe)
    print(f"Pedido: {cafe_com_leite.get_descricao()} | Custo: R${cafe_com_leite.get_custo():.2f}")

    # Adiciona açúcar ao café com leite
    cafe_completo = Acucar(cafe_com_leite)
    print(f"Pedido: {cafe_completo.get_descricao()} | Custo: R${cafe_completo.get_custo():.2f}")

    # Cria um café simples e adiciona apenas açúcar
    cafe_com_acucar = Acucar(CafeSimples())
    print(f"Pedido: {cafe_com_acucar.get_descricao()} | Custo: R${cafe_com_acucar.get_custo():.2f}")

    print("------------------------\n")
