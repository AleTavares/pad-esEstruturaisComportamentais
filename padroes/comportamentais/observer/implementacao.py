from abc import ABC, abstractmethod
from typing import List

# Interface do Observador
class Observer(ABC):
    """Define a interface para objetos que devem ser notificados sobre as mudanças em um Subject."""
    @abstractmethod
    def atualizar(self, noticia: str):
        """Este método é chamado quando o Subject é modificado.

        Args:
            noticia (str): A notícia a ser recebida.
        """
        pass

# Interface do Assunto (Subject)
class Subject(ABC):
    """Define a interface para objetos que podem ter assinantes."""
    @abstractmethod
    def adicionar_assinante(self, assinante: Observer):
        """Adiciona um assinante.

        Args:
            assinante (Observer): O assinante a ser adicionado.
        """
        pass

    @abstractmethod
    def remover_assinante(self, assinante: Observer):
        """Remove um assinante.

        Args:
            assinante (Observer): O assinante a ser removido.
        """
        pass

    @abstractmethod
    def notificar_assinantes(self):
        """Notifica todos os assinantes sobre uma mudança."""
        pass

# Assunto Concreto
class Editor(Subject):
    """Um Subject concreto que notifica os assinantes sobre novas notícias."""
    def __init__(self):
        """Inicializa o editor."""
        self._assinantes: List[Observer] = []
        self._noticia: str = ""

    def adicionar_assinante(self, assinante: Observer):
        """Adiciona um assinante à lista.

        Args:
            assinante (Observer): O assinante a ser adicionado.
        """
        print(f"Editor: {assinante.nome} começou a seguir.")
        self._assinantes.append(assinante)

    def remover_assinante(self, assinante: Observer):
        """Remove um assinante da lista.

        Args:
            assinante (Observer): O assinante a ser removido.
        """
        self._assinantes.remove(assinante)

    def notificar_assinantes(self):
        """Notifica todos os assinantes sobre uma nova notícia."""
        print("Editor: Notificando todos os assinantes...")
        for assinante in self._assinantes:
            assinante.atualizar(self._noticia)

    def publicar_noticia(self, noticia: str):
        """Publica uma nova notícia e notifica os assinantes.

        Args:
            noticia (str): A nova notícia.
        """
        self._noticia = noticia
        print(f'\nEditor: Nova notícia publicada: "{self._noticia}"')
        self.notificar_assinantes()

# Observador Concreto
class Assinante(Observer):
    """Um Observer concreto que recebe notificações do Editor."""
    def __init__(self, nome: str):
        """Inicializa o assinante com um nome.

        Args:
            nome (str): O nome do assinante.
        """
        self.nome = nome

    def atualizar(self, noticia: str):
        """Recebe a notícia e a exibe.

        Args:
            noticia (str): A notícia recebida.
        """
        print(f"Assinante {self.nome}: Recebeu a notícia: '{noticia}'")