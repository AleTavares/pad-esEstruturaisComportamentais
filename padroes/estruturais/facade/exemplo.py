from .implementacao import HomeTheaterFacade, Amplificador, DVDPlayer, Projetor

def main():
    """Função principal para demonstrar o uso do padrão Facade."""
    print("--- Padrão Facade ---")

    # Cria os componentes do subsistema
    amp = Amplificador()
    dvd = DVDPlayer()
    proj = Projetor()

    # Cria a fachada com os componentes
    home_theater = HomeTheaterFacade(amp, dvd, proj)

    # O cliente usa a fachada para realizar operações complexas com uma única chamada
    home_theater.assistir_filme("Design Patterns: O Filme")
    home_theater.parar_filme()

    print("---------------------\n")
