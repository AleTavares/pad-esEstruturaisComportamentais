# Classes do subsistema complexo
class Amplificador:
    """Representa um amplificador de áudio."""
    def ligar(self):
        """Liga o amplificador."""
        print("Amplificador ligado.")

    def desligar(self):
        """Desliga o amplificador."""
        print("Amplificador desligado.")

    def ajustar_volume(self, nivel):
        """Ajusta o volume do amplificador.

        Args:
            nivel (int): O nível do volume.
        """
        print(f"Volume do amplificador ajustado para {nivel}.")

class DVDPlayer:
    """Representa um DVD player."""
    def ligar(self):
        """Liga o DVD player."""
        print("DVD Player ligado.")

    def desligar(self):
        """Desliga o DVD player."""
        print("DVD Player desligado.")

    def play(self, filme):
        """Reproduz um filme.

        Args:
            filme (str): O nome do filme.
        """
        print(f'Reproduzindo filme: "{filme}".')

class Projetor:
    """Representa um projetor de vídeo."""
    def ligar(self):
        """Liga o projetor."""
        print("Projetor ligado.")

    def desligar(self):
        """Desliga o projetor."""
        print("Projetor desligado.")

# Fachada: simplifica a operação de assistir a um filme
class HomeTheaterFacade:
    """Fachada para simplificar a interação com o sistema de home theater."""
    def __init__(self, amp: Amplificador, dvd: DVDPlayer, proj: Projetor):
        """Inicializa a fachada.

        Args:
            amp (Amplificador): O amplificador.
            dvd (DVDPlayer): O DVD player.
            proj (Projetor): O projetor.
        """
        self.amplificador = amp
        self.dvd_player = dvd
        self.projetor = proj

    def assistir_filme(self, filme):
        """Liga o home theater e começa a assistir a um filme.

        Args:
            filme (str): O nome do filme.
        """
        print("\nPreparando para assistir filme...")
        self.projetor.ligar()
        self.amplificador.ligar()
        self.amplificador.ajustar_volume(10)
        self.dvd_player.ligar()
        self.dvd_player.play(filme)

    def parar_filme(self):
        """Para o filme e desliga o home theater."""
        print("\nFinalizando a sessão de filme...")
        self.dvd_player.desligar()
        self.amplificador.desligar()
        self.projetor.desligar()
